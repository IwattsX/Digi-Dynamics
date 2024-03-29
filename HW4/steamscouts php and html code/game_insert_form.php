<?php
    echo "Testing insert form <br>";

    //Declare variable
    $steamID = $_POST["ID"];
    $gameName = $_POST["name"];
    $supportInfo = $_POST["supportInfo"];
    $containsDLC = $_POST["containsDLC"];
    $bPrice = $_POST["bPrice"];
    $cPrice = $_POST["cPrice"];
    $developer = $_POST["developer"];
    $publisher = $_POST["publisher"];
    $genre = $_POST["genre"];
    $comingSoon = $_POST["comingSoon"];
    $date = $_POST["date"];
    $reqAge = $_POST["reqAge"];
    $cSupport = $_POST["cSupport"];
    $web = $_POST["web"];
    $sDescription = $_POST["sDescription"];
    $dDescription = $_POST["dDescription"];
    $sLanguage = $_POST["sLanguage"];
    $windows = $_POST["windows"];
    $linux = $_POST["linux"];
    $mac = $_POST["mac"];
    $header = $_POST["header"];

    
    

    //Displaying variable
    echo $steamID;
    echo "<br>";
    echo $gameName;
    echo "<br>";
    echo $supportInfo;
    echo "<br>";
    echo $containsDLC;
    echo "<br>";
    echo $bPrice;
    echo "<br>";
    echo $cPrice;
    echo "<br>";
    echo $developer;
    echo "<br>";
    echo $publisher;
    echo "<br>";
    echo $genre;
    echo "<br>";
    echo $comingSoon;
    echo "<br>";
    echo $date;
    echo "<br>";
    echo $reqAge;
    echo "<br>";
    echo $cSupport;
    echo "<br>";
    echo $web;
    echo "<br>";
    echo $sDescription;
    echo "<br>";
    echo $dDescription;
    echo "<br>";
    echo $sLanguage;
    echo "<br>";
    echo $windows;
    echo "<br>";
    echo $linux;
    echo "<br>";
    echo $mac;
    echo "<br>";
    echo $header;
    echo "<br>";

    $servername = "localhost";
    $username = "csci356_uni_db";
    $password = "1234";
    $dbname = "steamscout";

    // Create connection    
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $sql = "INSERT INTO games (ID, Name, Support_Info, Contains_DLC, Base_Price, Current_Price, Developer, Publisher, Genre, Coming_Soon, Release_Date, Required_Age, Controller_Support, Website, Short_Description, Detailed_Description, Supported_Language, Windows, Linux, Mac, Header_Image)
    VALUES ('$steamID', '$gameName', '$supportInfo', '$containsDLC', '$bPrice', '$cPrice', '$developer', '$publisher', '$genre', '$comingSoon', '$date', '$reqAge', '$cSupport', '$web', '$sDescription', '$dDescription', '$sLanguage', '$windows','$linux', '$mac', '$header')";
    

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();

?>