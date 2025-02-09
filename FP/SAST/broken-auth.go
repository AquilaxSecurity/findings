package main

import (
	"crypto/rand"
	"encoding/base64"
	"fmt"
	"html/template"
	"log"
	"net/http"
	"strings"
)

const (
	adminRole     = "admin"
	sessionCookie = "session_id"
	secureToken   = "super-secret-key"
)

var sessions = make(map[string]string)

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/admin", adminHandler)
	http.HandleFunc("/login", loginHandler)
	http.HandleFunc("/logout", logoutHandler)

	port := 1337
	addr := fmt.Sprintf("0.0.0.0:%d", port)
	fmt.Printf("Server listening on: http://%s\n", addr)
	log.Fatal(http.ListenAndServe(addr, nil))
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "To access admin, you must log in as an administrator.")
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	username := r.URL.Query().Get("username")

	if username == "admin" {
		sessionID := generateSessionID()
		sessions[sessionID] = adminRole

		http.SetCookie(w, &http.Cookie{
			Name:     sessionCookie,
			Value:    sessionID,
			HttpOnly: true, // Prevents JavaScript access
			Secure:   true, // Ensures HTTPS
			Path:     "/",
		})
		fmt.Fprintln(w, "Logged in successfully! Go to /admin")
	} else {
		fmt.Fprintln(w, "Invalid credentials")
	}
}

func adminHandler(w http.ResponseWriter, r *http.Request) {
	cookie, err := r.Cookie(sessionCookie)
	if err != nil {
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
		return
	}

	role, exists := sessions[cookie.Value]
	if !exists || role != adminRole {
		http.Error(w, "Forbidden", http.StatusForbidden)
		return
	}

	clientIP := strings.Split(r.RemoteAddr, ":")[0]
	if clientIP != "127.0.0.1" && clientIP != "localhost" {
		http.Error(w, "Access denied", http.StatusForbidden)
		return
	}

	tmpl := template.Must(template.New("admin").Parse(`<h1>Welcome, Admin!</h1>`))
	tmpl.Execute(w, nil)
}

func logoutHandler(w http.ResponseWriter, r *http.Request) {
	cookie, err := r.Cookie(sessionCookie)
	if err == nil {
		delete(sessions, cookie.Value) // Remove session
	}

	http.SetCookie(w, &http.Cookie{
		Name:   sessionCookie,
		Value:  "",
		MaxAge: -1,
		Path:   "/",
	})

	fmt.Fprintln(w, "Logged out successfully!")
}

func generateSessionID() string {
	b := make([]byte, 32)
	_, err := rand.Read(b)
	if err != nil {
		log.Fatal(err)
	}
	return base64.URLEncoding.EncodeToString(b)
}
