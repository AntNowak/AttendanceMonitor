<?php

    class dal{
        public function __construct(){}

        public function loginUser($username, $password){
            $sql = "SELECT username
                    FROM lecturer 
                    WHERE username = '$username' AND userPassword = '$password'";
            return $this -> query($sql)['0'] -> username;

        }
        public function getUser($user){
            $sql = "SELECT forename
                    FROM lecturer
                    WHERE username = '$user'";
                    return $this -> query($sql)['0'] ->forename;
        }

        //forms a connection to the chosen database 
        private function db(){

            $conn = mysqli_connect("localhost", "root","");
            mysqli_select_db($conn, 'testdatabase')
                or die ("Could not select the indicated database");//catch if database is not found during test connection        
            return $conn;
            
        }

        //constructs and poses query to the selected database using the public function above to get the SQL
        private function query($sql){   
                $res = mysqli_query($this->db(), $sql); 
                //checks for SELECT command  
                if ($res){
                    if (strpos($sql,'SELECT') === false){
                        return true;
                        }
                    }
                else{
                    if (strpos($sql,'SELECT') === false){
                        return false;
                        }
                    else{
                        return null;
                        }
                    }
                    
                $results = array();//array to hold any results found
                            
                while ($row = mysqli_fetch_array($res)){
                    $result = new DALQResults();                
                    foreach ($row as $k=>$v){
                        $result->$k = $v;
                        }
                    
                        $results[] = $result;
                    }
                    return $results;      
            }
        }
    
    //gets the results of a query from the database
    class DALQResults{

        private $_results = array();//privat array to hold results
 
        public function __construct(){}//constructor
        
        public function __set($var,$val){
            $this->_results[$var] = $val;
        }
        
        public function __get($var){  
            if (isset($this->_results[$var])){
            return $this->_results[$var];
            }
            else{
            return null;
            }
        }
    }
?>