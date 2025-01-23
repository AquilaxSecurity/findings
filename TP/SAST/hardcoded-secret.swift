import UIKit

class ViewController: UIViewController {

    let username = "admin"
    let password = "password"

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func loginButtonTapped(_ sender: UIButton) {
        let inputUsername = "admin"
        let inputPassword = "password"

        if inputUsername == username && inputPassword == password {
            print("Login successful")
        } else {
            print("Incorrect credentials")
        }
    }
}
