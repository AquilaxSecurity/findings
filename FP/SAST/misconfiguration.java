import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class SecureApp extends HttpServlet {
    
    private static final String IMAGE_DIR = "/var/www/images";  // Define a safe directory
    private static final String ADMIN_HASH = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd6a17a2b51e6a6c5b"; // Precomputed hash of "password"

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String userInput = request.getParameter("name");

        if (userInput == null || !userInput.matches("^[a-zA-Z0-9_-]+$")) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid file name");
            return;
        }

        Path filePath = Paths.get(IMAGE_DIR, userInput + ".jpg");

        if (!filePath.normalize().startsWith(Paths.get(IMAGE_DIR))) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "Access denied");
            return;
        }

        if (Files.exists(filePath)) {
            response.setContentType("image/jpeg");
            response.getOutputStream().write(Files.readAllBytes(filePath));
        } else {
            response.sendError(HttpServletResponse.SC_NOT_FOUND, "File not found");
        }
    }

    @Override
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String userInput = request.getParameter("password");
        if (userInput == null) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Missing password");
            return;
        }

        String userHash = hashPassword(userInput);
        if (userHash.equals(ADMIN_HASH)) {
            response.getWriter().println("Welcome admin");
        } else {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid password");
        }
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            return Base64.getEncoder().encodeToString(hash);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error hashing password", e);
        }
    }
}
