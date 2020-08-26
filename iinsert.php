<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
include('../includes/config.php');

if (isset($_GET['action'])) {
    if ($_GET['action'] == "insert") {
        $name = mysqli_real_escape_string($connection,trim($_GET['name']));
        $desc = mysqli_real_escape_string($connection,trim($_GET['desc']));
        $price = mysqli_real_escape_string($connection,trim($_GET['price']));
        $location = mysqli_real_escape_string($connection,trim($_GET['location']));
        $pic = mysqli_real_escape_string($connection,trim($_GET['pic']));
        $url = mysqli_real_escape_string($connection,trim($_GET['url']));
        $website = mysqli_real_escape_string($connection,trim($_GET['website']));
        
        $query = "INSERT INTO `items`(`name`, `desc`, `price`, `location`, `pic`, `url`, `website`) VALUES ('$name', '$desc', '$price', '$location', '$pic', '$url', '$website')";
        // echo $query;
        mysqli_query($connection, $query);
        $data['reply'] = "inserted";
        echo json_encode($data);
        
        exit;
    }
    if ($_GET['action'] == "duplicate") {
        $url = mysqli_real_escape_string($connection,str_replace(' ', '', $_GET['url']));
        $query = "SELECT id FROM `items` WHERE `url`='$url'";
        $result = mysqli_query($connection, $query);
        if (mysqli_num_rows($result) > 0) {
            $data['reply'] = "true";
        }
        else
        {
            $data['reply'] = "false";
        }
        echo json_encode($data);
        exit;
    }
}