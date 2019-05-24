<?php
    // 18 Oct 2017 - DB restored from db.sql after hack :(
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['username']) && isset($_POST['password'])) {
        $db = new mysqli('127.0.0.1', 'cs3284', 'cs3284', 'cs3284');
        $username = $_POST['username'];
        $password = $_POST['password'];
        $hashpass = sha1($password);
        // Allow old accounts that still have plaintext password as well as new
        // SHA1 accounts
        $stmt = $db->prepare("SELECT id FROM users WHERE username=? AND password IN (?, ?)");
        $stmt->bind_param("sss", $username, $password, $hashpass);
        $stmt->execute();
        $stmt->bind_result($id);
        if ($stmt->fetch()) {
            $_SESSION['id'] = $id;
            $_SESSION['username'] = $username;
            echo '<script type="text/javascript">window.location = "index.php?page=welcome"</script>';
            die();
        } else {
            $error = "No such user!";
        }
    }
?>
<form style="margin: 0 auto; width: 300px; text-align: center" method="POST" action="index.php?page=login">
    <h2 class="form-signin-heading">Login</h2>
    <?php if (isset($error)) { echo "<h3 style=\"color: red\">$error</h3>"; } ?>
    <label for="inputUsername" class="sr-only">Username</label>
    <input type="text" id="inputUsername" name="username" class="form-control" placeholder="Username" required autofocus>
    <label for="inputPassword" class="sr-only">Password</label>
    <input type="password" id="inputPassword" name="password" class="form-control" placeholder="Password" required>
    <br/>
    <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
</form>
