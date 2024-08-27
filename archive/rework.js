

for(let i = 1; i<headers.length; i++ ){
    const th = document.createElement("th");
    th.textContent = headers[i]
    thead.appendChild(th)
}




for(let i = 1; i<headers.length; i++ ){
    const td = document.createElement("td");
    td.textContent = row[headers[i]] !== null? row[headers[i]]:"";
    tr.appendChild(td)
}