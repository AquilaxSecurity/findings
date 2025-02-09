import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Scanner;
import java.util.HashMap;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import java.security.spec.InvalidKeySpecException;

public class SecureHashingDemo {

    private static final int ITERATIONS = 10000;
    private static final int KEY_LENGTH = 256;
    private static final String SECRET_PEPPER = "s3cr3tP3pp3r";
    private static HashMap<String, String[]> userDatabase = new HashMap<>();

    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeySpecException {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("1. Register\n2. Login\nChoose an option:");
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        if (choice == 1) {
            System.out.print("Enter new username: ");
            String username = scanner.nextLine();
            System.out.print("Enter new password: ");
            String password = scanner.nextLine();

            String salt = generateSalt();
            String hashedPassword = hashPassword(password, salt);

            userDatabase.put(username, new String[]{hashedPassword, salt});
            System.out.println("User registered successfully!");
            
        } else if (choice == 2) {
            System.out.print("Enter username: ");
            String username = scanner.nextLine();
            System.out.print("Enter password: ");
            String password = scanner.nextLine();

            if (userDatabase.containsKey(username)) {
                String[] storedData = userDatabase.get(username);
                String storedHash = storedData[0];
                String storedSalt = storedData[1];

                String inputHash = hashPassword(password, storedSalt);

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

    private static String hashPassword(String password, String salt) throws NoSuchAlgorithmException, InvalidKeySpecException {
        char[] chars = (password + SECRET_PEPPER).toCharArray();
        byte[] saltBytes = Base64.getDecoder().decode(salt);

        PBEKeySpec spec = new PBEKeySpec(chars, saltBytes, ITERATIONS, KEY_LENGTH);
        SecretKeyFactory skf = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");

        byte[] hash = skf.generateSecret(spec).getEncoded();
        return Base64.getEncoder().encodeToString(hash);
    }

    private static String generateSalt() {
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);
        return Base64.getEncoder().encodeToString(salt);
    }
}
