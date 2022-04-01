<?php include '302tax
.php'; ?>
<?php 
    $selfincome = $spouseincome = "";
    
    if ($_SERVER['REQUEST_METHOD'] == "POST") {
        if (empty($_POST['height'])) {
            $errh = "<span style='color:#ed4337; font-size:17px; display:block'>Height is requried</span>";
        } else {
            $height = validate($_POST['height']);
        }
    
        if (empty($_POST['weight'])) {
            $errw = "<span style='color:#ed4337; font-size:17px; display:block'>Weight is requried</span>";
        } else {
            $weight = validate($_POST['weight']);
        }

        if (empty($_POST['height'] && $_POST['weight'])) {
            echo "";
        } else {
            $MPF = ($weight / ($height * $height));
        }
    }
        if ($_POST['selfincome'] && empty($_POST['spouseincome']))
        $MPF = ($selfincome*0.05)
        $indiviual = 13200
        $Netincome = $selfincome - $MPF - $indiviual

        if ($_POST['spouseincome'] && empty($_POST['selfincome']))
        $MPF = ($selfincome*0.05)
        $indiviual = 13200
        $Netincome = $selfincome - $MPF - $indiviual



        if(empty($_POST['selfincome']) %% $_POST[''] )
    
    function validate($data){
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
?>