import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;
import java.util.HashMap;

public class InsecureHashingDemo {

    private static HashMap<String, String> userDatabase = new HashMap<>();

    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("1. Register\n2. Login\nChoose an option:");
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        if (choice == 1) {
            System.out.print("Enter new username: ");
            String username = scanner.nextLine();
            System.out.print("Enter new password: ");
            String password = scanner.nextLine();
            
            // Insecurely store password using weak hash
            String hashedPassword = insecureHash(password, "MD5");
            userDatabase.put(username, hashedPassword);
            System.out.println("User registered successfully!");
            
        } else if (choice == 2) {
            System.out.print("Enter username: ");
            String username = scanner.nextLine();
            System.out.print("Enter password: ");
            String password = scanner.nextLine();

            if (userDatabase.containsKey(username)) {
                String storedHash = userDatabase.get(username);
                String inputHash = insecureHash(password, "MD5");

                if (storedHash.equals(inputHash)) {
                    System.out.println("Login successful!");
                } else {
                    System.out.println("Invalid credentials.");
                }
            } else {
                System.out.println("User does not exist.");
            }
        }
        scanner.close();
    }

    private static String insecureHash(String input, String algorithm) {
        try {
            MessageDigest md = MessageDigest.getInstance(algorithm);
            md.update(input.getBytes());
            byte[] digest = md.digest();

            // Convert byte array to Hex String
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Hashing algorithm not found!", e);
        }
    }
}
