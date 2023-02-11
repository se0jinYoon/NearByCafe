const onClickLocationList = async (location) => {
    
    const res = await fetch('/cafe/find_cafe_ajax/', {
        method:"POST",
        headers:{
            "Content-Type":"application/x-www-form-urlencoded",
        },
        body:JSON.stringify({location:location}),//보내는거
    });

    // const res = await fetch('/cafe/find_cafe')
    // .then(console.log(Response))
    // .catch(console.log(console.error()))


    //받는거
    const {latitude:latitude, longtitude:longtitude, cafes:cafes} = await res.json();
    console.log(latitude,longtitude,cafes);

    cafeHandleResponse(cafes)

    

  
    
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

 