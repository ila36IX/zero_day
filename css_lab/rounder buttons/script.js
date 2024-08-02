const products112 = document.getElementsByClassName("product-item");
for (let i = 0; i < products112.length; i++) {

	const trigger = products112[i].getElementsByClassName('product-thumbnail');
	const hiddenBtn = products112[i].getElementsByClassName('product-actions');

	trigger[0].addEventListener('mouseenter', () => {
		hiddenBtn[0].style.display = 'block';
	});
	hiddenBtn[0].addEventListener('mouseenter', () => {
		hiddenBtn[0].style.display = 'block';
	});

	products112[0].addEventListener('mouseleave', () => {
		hiddenBtn[0].style.display = 'none';
	});
}