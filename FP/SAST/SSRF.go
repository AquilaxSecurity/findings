package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
)

var allowedDomains = []string{
	"https://example.com",
	"https://api.example.com",
}

func isAllowedURL(requestURL string) bool {
	parsedURL, err := url.Parse(requestURL)
	if err != nil {
		return false
	}

	for _, domain := range allowedDomains {
		if strings.HasPrefix(parsedURL.String(), domain) {
			return true
		}
	}

	return false
}

func fetchURL(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	requestURL := r.FormValue("url")

	if requestURL == "" {
		http.Error(w, "Missing URL parameter", http.StatusBadRequest)
		return
	}

	if !isAllowedURL(requestURL) {
		http.Error(w, "URL is not allowed", http.StatusForbidden)
		return
	}

	// Fetch the URL securely
	resp, err := http.Get(requestURL)
	if err != nil {
		http.Error(w, "Failed to fetch URL", http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	w.Header().Set("Content-Type", "text/plain")
	w.Header().Set("X-Content-Type-Options", "nosniff")

	io.Copy(w, resp.Body)
}

func main() {
	http.HandleFunc("/proxy", fetchURL)
	fmt.Println("Server running on port 8080...")
	http.ListenAndServe(":8080", nil)
}
