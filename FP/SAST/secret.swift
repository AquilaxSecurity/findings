import UIKit
import Security

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func loginButtonTapped(_ sender: UIButton) {
        let inputUsername = "admin"  
        let inputPassword = "password" 

        if authenticateUser(username: inputUsername, password: inputPassword) {
            print("Login successful")
        } else {
            print("Incorrect credentials")
        }
    }

    private func authenticateUser(username: String, password: String) -> Bool {
        guard let storedPassword = KeychainHelper.retrievePassword(for: username) else {
            return false
        }
        return storedPassword == password
    }
}

class KeychainHelper {

    static func storePassword(username: String, password: String) {
        let passwordData = password.data(using: .utf8)!
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: username,
            kSecValueData as String: passwordData
        ]
        SecItemAdd(query as CFDictionary, nil)
    }

    static func retrievePassword(for username: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: username,
            kSecMatchLimit as String: kSecMatchLimitOne,
            kSecReturnData as String: kCFBooleanTrue!
        ]
        var item: CFTypeRef?
        let status = SecItemCopyMatching(query as CFDictionary, &item)
        guard status == errSecSuccess, let passwordData = item as? Data else {
            return nil
        }
        return String(data: passwordData, encoding: .utf8)
    }
}
