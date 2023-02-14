
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

    likeHandleResponse(data.clicked);
}

const likeHandleResponse=(clicked)=>{
    var element=document.querySelector('.review_like');
    if(clicked=true){
        element.innerHTML=`♥좋아요`;
    }
    else{
        element.innerHTML=`♡좋아요`;
    }
    
};
