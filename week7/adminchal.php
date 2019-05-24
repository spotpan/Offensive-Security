<?php
    if (!isset($_SESSION['id']) || $_SESSION['id'] !== 1) {
        echo '<script type="text/javascript">window.location = "index.php?page=welcome"</script>';
        die();
    }

    if (isset($_POST["submit"])) {
        $target_fn = "uploads/" . basename($_FILES["uploaded"]["name"]);
        move_uploaded_file($_FILES["uploaded"]["tmp_name"], $target_fn);
    }
?>
<h1>Admin panel</h1>
<br/>
<h2>Posts:</h2>
<p>Under development!</p>
<br/>
<h2>Media:</h3>
<form action="index.php?page=admin" method="post" enctype="multipart/form-data">
    Select file to upload:
    <input type="file" name="uploaded" id="uploaded">
    <input type="submit" value="Upload File" name="submit">
</form>
<ul>
<?php
    foreach (scandir("uploads/") as $file) {
        if ($file !== "." && $file !== "..")
            echo "<li><a href=\"uploads/$file\">$file</a></li>\n";
    }
?>
</ul>
