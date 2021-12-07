

var updateBtns = document.getElementsByClassName('update-cart')//클래스 이름으로 찾고 updateBtns에 저장

for (i = 0; i < updateBtns.length; i++) {//for문을 돌리는 이유는 모든 updateBtns에게 기능을 추가하기 위함이다.
	updateBtns[i].addEventListener('click', function(){ //클릭시 function 실행
		var productId = this.dataset.product;//커스텀 attribute를 통해 데이터를 가져옴 즉, store.html에 있는 product.id가져옴
		var action = this.dataset.action;// add가져옴 this는 클릭이 된애
		console.log('productId:', productId, 'Action:', action);

		console.log("User:", user)
		if (user == 'AnonymousUser') {
			addCookieItem(productId, action)
		} else { //로그인이 되어있다면 제품ID, 수행할 action 전달
			updateUserOrder(productId,action)

		}

	})
}

function addCookieItem(productId, action) {
	console.log('Not logged in...')

	if (action == 'add') {
		if (cart[productId] == undefined) {
			cart[productId] = {'quantity': 1}
		}else{
			cart[productId]['quantity'] += 1
		}
	}
	if(action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0) {
			console.log('Remove Item')
			delete cart[productId]
		}
	}
	console.log('Cart:', cart);
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()

}

function updateUserOrder(productId, action) {
	console.log("user is logged in, sending data")
	var url ='/update_item/' //데이터 보낼 위치 즉, 해당 url은 updateItem을 부르고 있으므로 updateItem에게 전달

	fetch(url,{ //fetch는 promise based이다. 즉, then과 catch를 사용할 수 있다.
		method: 'POST',
		headers:{ //json을 주기 위해서 fectch에게 headers를 사용해서 json을 준다는거 말해줘야한다.
			'Content-Type': 'applictaion/json',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({'productId':productId, 'action':action})
	})
	.then((response)=>{ //promise란 말그대로 약속, resolve혹은 reject를 받고난후 then실행
		return response.json() //view에 있는 updateItem으로 부터 JsonResponse를 받음
	})
	.then((data)=>{
		location.reload()
		console.log('data:',data)
		// location.reload()
	})
}

// var updateBtns = document.getElementsByClassName('update-cart')//클래스 이름으로 찾고 updateBtns에 저장
//
// for (i = 0; i < updateBtns.length; i++) { //for문을 돌리는 이유는 모든 updateBtns에게 기능을 추가하기 위함이다.
// 	updateBtns[i].addEventListener('click', function(){ //클릭시 function 실행
// 		var productId = this.dataset.product //커스텀 attribute를 통해 데이터를 가져옴 즉, store.html에 있는 product.id가져옴
// 		var action = this.dataset.action // add가져옴 this는 클릭이 된애
// 		console.log('productId:', productId, 'Action:', action)
//
//     })
// }

