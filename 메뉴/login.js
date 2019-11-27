function login()
{
    var id = document.getElementById("id");
    var pw = document.getElementById("pw");
    
    if(id.value == "aqi222")
    {
        if(pw.value == "1234")
        {
            
            localStorage.setItem('username',id.value);
            localStorage.getItem('username');
            alert(id.value + "님, 환영합니다.");
            window.location.href="user.html";
           
        }
        else{
            alert("비밀번호를 잘못 입력하셨습니다.");
            
        }
    }
    else
    {
        alert("다시 시도해 보세요");
    }

}
