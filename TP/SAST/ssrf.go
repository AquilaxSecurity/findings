package main

import (
	"fmt"
	"io"
	"net/http"
)

func fetchURL(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	url := r.FormValue("url") 

	if url == "" {
		http.Error(w, "Missing URL parameter", http.StatusBadRequest)
		return
	}

	resp, err := http.Get(url)
	if err != nil {
		http.Error(w, "Failed to fetch URL", http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	io.Copy(w, resp.Body)
}

func main() {
	http.HandleFunc("/proxy", fetchURL)
	fmt.Println("Server running on port 8080...")
	http.ListenAndServe(":8080", nil)
}
