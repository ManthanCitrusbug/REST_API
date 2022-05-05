function validate(){
    const username = document.getElementById("id_username").value;
    const f_name = document.getElementById("id_first_name").value;
    const l_name = document.getElementById("id_last_name").value;
    const email = document.getElementById("id_email").value;
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const password = document.getElementById("id_password").value;
    const c_password = document.getElementById("id_confirm_password").value;
    // var submition = 1;

    if(username == ""){
        document.getElementById("error_username").innerHTML = "Enter you're User name.";
        user_submition = 0;
    }

    else if(!isNaN(username) || (!isNaN(username[0]))){
        document.getElementById("error_username").innerHTML = "First latter must be alphabet."
        user_submition = 0;
    }

    else{
        document.getElementById("error_username").innerHTML = "";
        user_submition = 1;
    }

    if(f_name == ""){
        document.getElementById("error_f_name").innerHTML = "Enter you're First name.";
        f_name_submition = 0;
    }

    else if(!isNaN(f_name) || (!isNaN(f_name[0]))){
        document.getElementById("error_f_name").innerHTML = "First latter must be alphabet."
        f_name_submition = 0;
    }

    else{
        document.getElementById("error_f_name").innerHTML = "";
        f_name_submition = 1;
    }

    if(l_name == ""){
        document.getElementById("error_l_name").innerHTML = "Enter you're Last name.";
        l_name_submition = 0;
    }

    else if(!isNaN(l_name) || (!isNaN(l_name[0]))){
        document.getElementById("error_l_name").innerHTML = "First latter must be alphabet."
        l_name_submition = 0;
    }

    else{
        document.getElementById("error_l_name").innerHTML = "";
        l_name_submition = 1;
    }


    if(email == ""){
        document.getElementById("error_email").innerHTML = "Enter your Mail ID";
        email_submition = 0;

    }
    else if(!isNaN(email)){
        document.getElementById("error_email").innerHTML = "Alphabests are not allowed";
        email_submition = 0;

    }
    else if(validRegex.test(email)==false){
        document.getElementById("error_email").innerHTML = "Enter valid email.";
        email_submition = 0;
    }
    else{
        document.getElementById("error_email").innerHTML = "";
        email_submition = 1;
    }

    if(password == ""){
        document.getElementById("error_password").innerHTML = "Enter your password.";
        pass_submition = 0;
    }

    else if((password.length <= 6) || (password.length >= 13)){
        document.getElementById("error_password").innerHTML = "Password must be in 6 to 13 charactors.";
        pass_submition = 0;
    }

    else{
        document.getElementById("error_password").innerHTML = "";
        pass_submition = 1;
    }

    if(c_password == ""){
        document.getElementById("error_c_password").innerHTML = "Confirm your password."
        c_pass_submition = 0;
    }

    else if(password != c_password){
        document.getElementById("error_c_password").innerHTML = "Your password doesn't match."
        c_pass_submition = 0;
    }

    else if((password.length <= 6) || (password.length >= 13)){
        document.getElementById("error_password").innerHTML = "Password must be in 6 to 13 charactors.";
        c_pass_submition = 0;
    }

    else{
        document.getElementById("error_c_password").innerHTML = "";
        c_pass_submition = 1;
    }

    if(user_submition===1 & f_name_submition===1 & l_name_submition===1 & email_submition===1 & pass_submition===1 & c_pass_submition===1){
        return true;
    }
    else{
        return false;
    }
}

function login_validate(){
    const username = document.getElementById("id_username").value;
    const password = document.getElementById("id_password").value;

    if(username == ""){
        document.getElementById("error_email").innerHTML = "Enter your Username";
        email_submition = 0;

    }
    else if(!isNaN(username)){
        document.getElementById("error_email").innerHTML = "Alphabests are not allowed";
        email_submition = 0;

    }
    else{
        document.getElementById("error_email").innerHTML = "";
        email_submition = 1;
    }

    if(password == ""){
        document.getElementById("error_password").innerHTML = "Enter your password.";
        pass_submition = 0;
    }

    else if((password.length <= 6) || (password.length >= 13)){
        document.getElementById("error_password").innerHTML = "Password must be in 6 to 13 charactors.";
        pass_submition = 0;
    }

    else{
        document.getElementById("error_password").innerHTML = "";
        pass_submition = 1;
    }

    if(email_submition===1 & pass_submition===1){
        return true;
    }
    else{
        return false;
    }
}


function book_validate(){
    const name = document.getElementById("id_name").value;
    const disc = document.getElementById("id_description").value;
    const category = document.getElementById("id_category").value;
    const quantity = document.getElementById("id_quantity").value;


    if(name == ""){
        document.getElementById("error_product_name").innerHTML = "Enter you're User name.";
        user_submition = 0;
    }

    else{
        document.getElementById("error_product_name").innerHTML = "";
        user_submition = 1;
    }


    if(disc == ""){
        document.getElementById("error_product_disc").innerHTML = "Enter Book Dicription.";
        disc_submition = 0;
    }
    else{
        document.getElementById("error_product_disc").innerHTML = "";
        disc_submition = 1;
    }

    if(category == ""){
        document.getElementById("error_product_category").innerHTML = "Select Book Category.";
        cate_submition = 0;
    }
    else{
        document.getElementById("error_product_category").innerHTML = "";
        cate_submition = 1;
    }

    if(quantity == ""){
        document.getElementById("error_quantity").innerHTML = "Enter Book Quantity.";
        qun_submition = 0;
    }
    else if(isNaN(quantity)){
        document.getElementById("error_quantity").innerHTML = "Enter a valid Book quantity."
        qun_submition = 0;
    }
    else if(quantity<=0){
        document.getElementById("error_quantity").innerHTML = "Enter a valid Book quantity."
        qun_submition = 0;
    }
    else{
        document.getElementById("error_quantity").innerHTML = "";
        qun_submition = 1;
    }

    if((user_submition===1) & (disc_submition===1) & (cate_submition===1) & (qun_submition===1)){
        return true;
    }
    else{
        return false;
    }
}



function author_validate(){
    const name = document.getElementById("id_name").value;
    const disc = document.getElementById("id_description").value;

    if(name == ""){
        document.getElementById("error_product_name").innerHTML = "Enter you're User name.";
        user_submition = 0;
    }

    else if(!isNaN(name) || (!isNaN(name[0]))){
        document.getElementById("error_product_name").innerHTML = "Enter valid Name."
        user_submition = 0;
    }

    else{
        document.getElementById("error_product_name").innerHTML = "";
        user_submition = 1;
    }
    if(disc == ""){
        document.getElementById("error_product_disc").innerHTML = "Enter Book Dicription.";
        disc_submition = 0;
    }
    else{
        document.getElementById("error_product_disc").innerHTML = "";
        disc_submition = 1;
    }

    if((user_submition===1) & (disc_submition===1)){
        return true;
    }
    else{
        return false;
    }
}




function issue_book(){
    const name = document.getElementById("id_username").value;
    const email = document.getElementById("id_email").value;
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const address = document.getElementById("id_address").value;
    const book = document.getElementById("id_book").value;
    const issued_date = document.getElementById("id_issued_date").value;
    const charge_per_day = document.getElementById("id_charge_per_day").value;


    if(name == ""){
        document.getElementById("error_username").innerHTML = "Enter User Name.";
        name_submition = 0;
    }
    else{
        document.getElementById("error_username").innerHTML = "";
        name_submition = 1;
    }

    if(email == ""){
        document.getElementById("error_email").innerHTML = "Enter your Mail ID";
        email_submition = 0;

    }
    else if(!isNaN(email)){
        document.getElementById("error_email").innerHTML = "Alphabests are not allowed";
        email_submition = 0;

    }
    else if(validRegex.test(email)==false){
        document.getElementById("error_email").innerHTML = "Enter valid email.";
        email_submition = 0;
    }
    else{
        document.getElementById("error_email").innerHTML = "";
        email_submition = 1;
    }


    if(address == ""){
        document.getElementById("error_address").innerHTML = "Enter Book Dicription.";
        disc_submition = 0;
    }
    else{
        document.getElementById("error_address").innerHTML = "";
        disc_submition = 1;
    }

    if(book == ""){
        document.getElementById("error_book").innerHTML = "Select Book Category.";
        cate_submition = 0;
    }
    else{
        document.getElementById("error_book").innerHTML = "";
        cate_submition = 1;
    }

    if(issued_date == ""){
        document.getElementById("error_issued_date").innerHTML = "Enter Issued Date.";
        disc_submition = 0;
    }
    else{
        document.getElementById("error_issued_date").innerHTML = "";
        disc_submition = 1;
    }


    if(charge_per_day == ""){
        document.getElementById("error_charge_per_day").innerHTML = "Enter Charge Per Day.";
        chr_submition = 0;
    }
    else if(isNaN(charge_per_day)){
        document.getElementById("error_charge_per_day").innerHTML = "Enter a Number."
        chr_submition = 0;
    }
    else if(charge_per_day<=0){
        document.getElementById("error_charge_per_day").innerHTML = "Enter a valid Charge."
        chr_submition = 0;
    }
    else{
        document.getElementById("error_charge_per_day").innerHTML = "";
        chr_submition = 1;
    }

    if((name_submition===1) & (disc_submition===1) & (cate_submition===1) & (chr_submition===1)){
        return true;
    }
    else{
        return false;
    }
}



function search_data(){
    const search = document.getElementById('search').value;
    console.log(search);
}