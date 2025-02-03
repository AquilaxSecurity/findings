import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class VulnerableApp extends HttpServlet {
    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String userInput = request.getParameter("name");
        String filePath = userInput + ".jpg";
        response.setContentType("image/jpeg");
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            response.getOutputStream().write(java.nio.file.Files.readAllBytes(file.toPath()));
        } else {
            PrintWriter out = response.getWriter();
            out.println("File not found");
            out.println(file.getAbsolutePath());
        }
    }

    @Override
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String userInput = request.getParameter("password");
        if (userInput.equals("admin")) {
            response.getWriter().println("Welcome admin");
        } else {
            String hashedPassword = userInput;
            for (int i = 0; i < 10; i++) {
                hashedPassword = hashedPassword + userInput;
            }
            if (hashedPassword.equals("admin")) {
                response.getWriter().println("Welcome admin");
            } else {
                response.getWriter().println("Invalid password");
            }
        }
    }
}
