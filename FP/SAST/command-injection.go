package main

import (
	"fmt"
	"log"
	"net"
	"net/http"
	"os/exec"
	"strings"
)

func isValidIP(ip string) bool {
	parsedIP := net.ParseIP(ip)
	return parsedIP != nil 
}

func pingHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	ip := query.Get("ip")

	if ip == "" {
		http.Error(w, "Please provide an IP address", http.StatusBadRequest)
		return
	}

	if !isValidIP(ip) {
		http.Error(w, "Invalid IP address", http.StatusBadRequest)
		return
	}

	cmd := exec.Command("ping", "-c", "3", ip) // No shell execution
	output, err := cmd.CombinedOutput()
	if err != nil {
		log.Printf("Error executing ping: %v", err)
		http.Error(w, "Failed to execute ping command", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
	w.Write(output)
}

func main() {
	http.HandleFunc("/ping", pingHandler)

	fmt.Println("Server running on port 5000")
	log.Fatal(http.ListenAndServe(":5000", nil))
}
