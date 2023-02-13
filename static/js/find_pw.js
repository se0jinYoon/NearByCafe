const strip = (string) => {
    return string.replace(/^\s+|\s+$/g, "");
};

// const requestFindPw=new XMLHttpRequest();

// const onClickFindPw=()=>{
//     const url='User/views/find_pw'; //?
//     var find_email=document.getElementsByName('find_pw_email').value;
//     requestFindPw.open('POST',url,true)
//     requestFindPw.setRequestHeader(
//         "Content-Type",
//         "application/x-www-form-urlencoded"
//     );

//     requestFindPw.send(JSON.stringify({find_email:find_email}));
// };

// requestFindPw.onreadystatechange=()=>{
//     if(requestFindPw.readyState==XMLHttpRequest.DONE){
//         if(requestCommentCreate.status<400){
//             const {findOrNot,find_email}=Json.parse(requestFindPw.response);

//             if (findOrNot==True){//일치하는 pw찾았을때, 비밀번호 재설정 링크 안내 모달
//                 var modal=document.getElementById('reset_link_modal')// ! 재설정 모달로 지정
//             }

//             else{//일치하는 pw 없을때
//                 var modal=document.getElementById('no_email_modal')  //일치 이메일 없음 안내 모달
//             }

//             $('#modal').modal("show");

//     }
// }
// }

//방법2
// if ($(".findpw_input"));

const onClickFindPw=()=>{
    find_email = document.querySelector(".findpw_input");

    $.ajax({
        url: "{% url 'User:find_pw' %}",
        data: {
            find_email: find_email.value,
        },
        datatype: "json",
        success: function (data) {
            if (data["overlap"] == "fail") {
                //일치 이메일 없음 안내 모달 띄우기
                var modal = document.getElementById("no_email_modal"); //일치 이메일 없음 안내 모달
            } else {
                //비번 재설정 안내 모달
                var modal = document.getElementById("reset_link_modal"); // ! 재설정 모달로 지정
            }
            $("#modal").modal("show");
        },
    });
}
