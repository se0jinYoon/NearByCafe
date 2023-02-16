
const onClickLocationList = async (location) => {

    //선택 키워드 뽑아내기
    var seleted_ck=[];

    $("input[name=checkbox]:checked").each(function(){
            var chk=$(this).val();
        seleted_ck.push(chk);
    })
    
    const res = await fetch('/find_cafe_ajax/', {
        method:"POST",
        headers:{
            "Content-Type":"application/x-www-form-urlencoded",
        },
        body:JSON.stringify({location:location,seleted_ck:seleted_ck}),//보내는거
    });

    // const res = await fetch('/cafe/find_cafe')
    // .then(console.log(Response))
    // .catch(console.log(console.error()))

    //받는거
    const {latitude:latitude, longtitude:longtitude, cafes:cafes} = await res.json();
    console.log(latitude,longtitude,cafes);
    cafeHandleResponse(cafes);
    panTo(latitude,longtitude);

}


const cafeHandleResponse = (cafes) => {
    var element = document.querySelector(".cafe_list");
    element.innerHTML = `<div class="cafe_list">`
    cafes.forEach(item => {
        element.innerHTML +=  `
        <div class="cafe d-flex">
        <span class="cafe_name">${item.name}</span>                    
        <span class="cafe_loc">${item.address}</span>         
        <span class="cafe_categ">#공부하기 좋은 #분위기 예쁜 #저렴한</span> 
        <div class="cafe_star_info">             
            <span style="color: #F8AA14">3.0</span>                     
            <span>⭐️⭐️⭐️⭐️⭐️</span>                
            <span style="color: #AAAAAA">(65)</span>                    
        </div>
    </div>`
        
    });
   
}

//전달받은 위치의 위도,경도로 카카오맵 이동
const panTo=(latitude,longtitude)=>{
    var moveLatLon=new kakao.maps.LatLng(latitude,longtitude);
    var markerPosition = new kakao.maps.LatLng(latitude,longtitude);
    var marker = new kakao.maps.Marker({
        position : markerPosition
    })
    marker.setMap(map);
    map.panTo(moveLatLon);
  
}



