
cnt=0
const onClickLike=async(id)=>{
    
    //좋아요 눌렀을때
    if (cnt==0){
        clicked=true
        cnt+=1
    }
    //취소 눌렀을때
    else{
        clicked=false
        cnt==0
    }

    const url="/cafe_like/"
    const {data}=await axios.post(url,{
        id,clicked
    });

    likeHandleResponse(data.id,data.clicked);
    //한번 더 눌렀을땐 취소인거 추가~

}

const likeHandleResponse=(id,clicked)=>{
    //좋아요 누른 경우
    if(clicked=true){
    //좋아요 색 채워지는 html 추가해주세요!-to 프론트

    }
    else{
    //한번 더 눌러서 좋아요 취소되는거라 하트색 다시 없어지는 html 추가해주세요~
    }
    
}

const onClickLikeNotLogin=()=>{
    const url="/like_denied/"
    //모달 보내는 요청만 보내기
}