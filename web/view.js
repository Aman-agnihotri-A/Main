$("#alogin").hide();
$("#insert").hide();
$("#delete").hide();
 


function dim()
{  
let Username=$('#Username').val()
let password=$('#passwd').val()
console.log(Username)
console.log(password)
   
eel.login(Username,password)(givetopython)
}

function givetopython(result)
{
   if (result=="success")
   {
   $("#alogin").show();
   $("#blogin").hide();
   alert("LOGIN SUCCESFULL");
   
   }
   else{ 
   $("#blogin").show();
   $("#alogin").hide();
}
   
}
function simp(){
   $('#Username').val("")
   $('#passwd').val("")
   $("#alogin").hide();
   $("#blogin").show();
   


}

function assign_room()
{
  
   eel.assign_rooms()
   
}
function room(res)
{
   alert("ROOMS HAVE BEEN ASSIGNED SUCCESFULLY");
}
function create()
{
   eel.create_Table()
   alert("DATABASE HAVE BEEN CREATED");
}
function mass_load_student()
{
   eel.mass_load_student()
   alert("STUDENT DATA HAS BEEN INSERTED");
}
function mass_load_teach()
{
   eel.mass_load_Teachers()
   alert("TEACHER DATA HAS BEEN INSERTED");
}
function mass_load_room()
{
   eel.mass_load_rooms()
   alert("ROOMS DATA HAS BEEN INSERTED");
}
function random_teacher()
{
   eel.example_extract()
   alert("TEACHERS HAVE BEEN ALLOTED");
}
function insert()
{
  
   $("#alogin").hide();
   $("#insert").show();
}

function ins()

{
   let teach=$('#id').val()
   let fname=$('#fname').val()
   let lname=$('#lname').val()
   let cid=$('#cid').val()
   console.log(teach)
   console.log(fname)
   console.log(lname)
   console.log(cid)
   eel.single_load_Teachers(teach,fname,lname,cid)(givetopython)
   alert("TEACHERS DATA INSERTED");
   

}
function back()
{
   $("#alogin").show();
   $("#insert").hide();
}
function bac()
{
   $("#alogin").show();
   $("#delete").hide();
}
function d()
{
   $("#alogin").hide();
   $("#blogin").hide();
   $("#delete").show();
   
}
function del()
{
   let teachid=$('#tid').val()
   console.log(teachid)
   eel.delete_single_Teachers(teachid)(givetopython)
   alert("TEACHERS DATA DELETED");
  


}
