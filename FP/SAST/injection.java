package com.example.demo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Set;

@RestController
@RequestMapping("/users")
public class UserController {

    private final JdbcTemplate jdbcTemplate;

    private static final Set<String> ALLOWED_SORT_COLUMNS = Set.of("id", "username", "created_at");

    public UserController(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @GetMapping
    public List<Map<String, Object>> getUsers(@RequestParam(defaultValue = "id") String orderBy) {
        if (!ALLOWED_SORT_COLUMNS.contains(orderBy)) {
            throw new IllegalArgumentException("Invalid sort column.");
        }
        
        String query = "SELECT * FROM users ORDER BY " + orderBy;
        return jdbcTemplate.queryForList(query);
    }

    @PostMapping
    public String addUser(@RequestParam String username) {
        if (username == null || username.trim().isEmpty()) {
            return "Username cannot be empty";
        }

        String sanitizedUsername = username.replaceAll("[^a-zA-Z0-9]", "");
        String query = "INSERT INTO users (username) VALUES (?)";
        jdbcTemplate.update(query, sanitizedUsername);
        return "User added successfully";
    }
}
