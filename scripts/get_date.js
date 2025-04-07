function showTime() {
	const date = new Date();

	let today = date.toLocaleString("en", { weekday: "long" });
	let time = date.toLocaleTimeString("en", { hour12: true }); // full time string with AM/PM
	let day = date.toLocaleString("en", { day: "2-digit" });
	let month = date.toLocaleString("en", { month: "2-digit" });
	let year = date.toLocaleString("en", { year: "numeric" });

	document.getElementById(
		"date-display"
	).innerHTML = `${today}, ${time} | ${day}/${month}/${year}`;
	setTimeout(showTime, 0);
}

showTime();
