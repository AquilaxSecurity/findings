package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sync"
)

type User struct {
	Username string `json:"username"`
	Password string `json:"password"`
	Role     string `json:"role"` 
}

var (
	users = map[string]*User{
		"user1":  {Username: "user1", Password: "password", Role: "user"},
		"admin":  {Username: "admin", Password: "admin", Role: "admin"},
	}
	mu sync.Mutex
)

func updateProfile(w http.ResponseWriter, r *http.Request) {
	var updatedUser User
	if err := json.NewDecoder(r.Body).Decode(&updatedUser); err != nil {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}

	mu.Lock()
	defer mu.Unlock()

	user, exists := users[updatedUser.Username]
	if !exists {
		http.Error(w, "User not found", http.StatusNotFound)
		return
	}

	*user = updatedUser

	fmt.Fprintf(w, "Profile updated successfully: %+v", user)
}

func main() {
	http.HandleFunc("/update_profile", updateProfile)
	fmt.Println("Server running on port 8080...")
	http.ListenAndServe(":8080", nil)
}
