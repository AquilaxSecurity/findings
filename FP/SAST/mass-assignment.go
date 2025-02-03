package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sync"

	"golang.org/x/crypto/bcrypt"
)

type User struct {
	Username string `json:"username"`
	Password string `json:"-"` // Do not expose password in JSON
	Role     string `json:"role"`
}

var (
	users = map[string]*User{
		"user1":  {Username: "user1", Password: hashPassword("password"), Role: "user"},
		"admin":  {Username: "admin", Password: hashPassword("admin"), Role: "admin"},
	}
	mu sync.Mutex
)

func hashPassword(password string) string {
	hashed, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		panic(err) // Proper error handling should be implemented
	}
	return string(hashed)
}

func updateProfile(w http.ResponseWriter, r *http.Request) {
	var updatedData struct {
		Username string `json:"username"`
		Password string `json:"password"`
	}

	if err := json.NewDecoder(r.Body).Decode(&updatedData); err != nil {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}

	mu.Lock()
	defer mu.Unlock()

	user, exists := users[updatedData.Username]
	if !exists {
		http.Error(w, "User not found", http.StatusNotFound)
		return
	}

	user.Password = hashPassword(updatedData.Password)

	fmt.Fprintf(w, "Profile updated successfully for %s", user.Username)
}

func main() {
	http.HandleFunc("/update_profile", updateProfile)
	fmt.Println("Server running on port 8080...")
	http.ListenAndServe(":8080", nil)
}
