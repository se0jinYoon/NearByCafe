const strip = (string) => {
    return string.replace(/^\s+|\s+$/g, "");
};
cnt=0
// <button class="review_like d-flex" data-bs-toggle="modal" data-bs-target="#not_login" onclick="onClickLike({{cafe.id}}">♡좋아요</button>
const onClickLike=async(id,clicked)=>{
    console.log(clicked,cnt)
    
     //좋아요 눌렀을때
    if (cnt==0){
        clicked=true
        cnt+=1
    }
    //취소 눌렀을때
    else{
        clicked=false
        cnt=0
    }
    console.log(clicked)
    

    const url="/cafe_like/"
    const {data}=await axios.post(url,{
        id,clicked,
    });

    
    likeHandleResponse(data.id,data.clicked);
}

const likeHandleResponse=(id,clicked)=>{
    console.log(clicked)
    
    const element=document.querySelector('.review_like');
    const orginhtml=element.innerHTML;
    if(clicked===true){
        element.innerHTML=`♥좋아요`;
    }
    else{
        element.innerHTML=`♡좋아요`;
    }
    
};
