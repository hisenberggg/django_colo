<?php
	session_start();
	
	 $host="localhost";
	 $username="root";
	 $password="";
	 $databasename="games";
	 $connect=mysqli_connect($host,$username,$password,$databasename);

	 $score=$_POST['score1'];
	 
	 $sql = "INSERT INTO score(highscore) VALUES('$score')";

	 $select_data=mysqli_query($connect,$sql);
	 if($row=mysqli_fetch_array($select_data))
	 {
	  echo "success";
	 }
	 else
	 {
	  echo "Error inserting";
	 }
	 exit();
	
?>


<!-- <?php
	session_start();
	
	 $host="localhost";
	 $username="root";
	 $password="";
	 $databasename="games";
	 $connect=mysqli_connect($host,$username,$password,$databasename);
	 

	 $score=$_POST['score1'];
	 $tablename = "scores";

	 
	 $sql = "UPDATE $tablename SET score = '$score'  WHERE id = 1";

	
	 if ($connect->query($sql) === TRUE)
 	{
 		echo "Success";
 	}
 	else
 	{
 		echo "Fail";
 	}
	
?> -->