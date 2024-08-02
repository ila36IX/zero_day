const products1 = document.getElementsByClassName("product-item");
for (let i = 0; i < products1.length; i++) {
    products1[i].style.position = "relative";
    const after = Number(products1[i].querySelector(".product-price span.after .value").textContent);
    const before = Number(products1[i].querySelector(".product-price span.before .value").textContent);
    const discount = 100 - (after / before) * 100
    products1[i].insertAdjacentHTML("afterbegin", '<span style="z-index: 99; direction: ltr; position: absolute; top: 10px; right: 10px; background-color: #ff9800; border-radius: 15px; padding: 3px 6px; color: #fff; font-size: 16px; margin-left: 0;">' + -1 * Math.floor(discount) + '%</span>');
}

