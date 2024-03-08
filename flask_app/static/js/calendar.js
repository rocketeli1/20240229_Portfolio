document.addEventListener("DOMContentLoaded", function () {
    const calendar = document.getElementById("calendar");
    const prevMonthBtn = document.getElementById("prev-month");
    const nextMonthBtn = document.getElementById("next-month");
    const monthHeader = document.getElementById("month-header");

    let currentYear = new Date().getFullYear();
    let currentMonth = new Date().getMonth();

    // Render the calendar for the current month and year
    renderCalendar(currentYear, currentMonth);

    // Fetch events and render them
    fetchAndRenderEvents();

    // Event listener for previous month button
    prevMonthBtn.addEventListener("click", function () {
        currentMonth -= 1;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear -= 1;
        }
        renderCalendar(currentYear, currentMonth);
        fetchAndRenderEvents();
    });

    // Event listener for next month button
    nextMonthBtn.addEventListener("click", function () {
        currentMonth += 1;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear += 1;
        }
        renderCalendar(currentYear, currentMonth);
        fetchAndRenderEvents();
    });

    // Function to render the calendar for the given year and month
    function renderCalendar(year, month) {
        calendar.innerHTML = "";

        const firstDayOfMonth = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        monthHeader.textContent = new Date(year, month).toLocaleString('default', { month: 'long', year: 'numeric' });

        // Array to store the days of the week
        const weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

        // Create header row for days of the week
        const headerRow = document.createElement("div");
        headerRow.classList.add("header-row");
        weekDays.forEach(day => {
            const header = document.createElement("div");
            header.classList.add("header");
            header.textContent = day;
            headerRow.appendChild(header);
        });
        calendar.appendChild(headerRow);

        let dayCount = 1;

        // Create rows for each week
        for (let i = 0; i < 6; i++) {
            const week = document.createElement("div");
            week.classList.add("week");
            for (let j = 0; j < 7; j++) {
                if (i === 0 && j < firstDayOfMonth) {
                    const emptyDay = document.createElement("div");
                    emptyDay.classList.add("day");
                    week.appendChild(emptyDay);
                } else if (dayCount > daysInMonth) {
                    break;
                } else {
                    const day = document.createElement("div");
                    day.classList.add("day");
                    day.textContent = dayCount;
                    day.dataset.day = dayCount; // Add dataset for event matching
                    week.appendChild(day);
                    dayCount++;
                }
            }
            calendar.appendChild(week);
        }
    }

    // Function to fetch events from the backend server and render them
    function fetchAndRenderEvents() {
        fetch(`/events?year=${currentYear}&month=${currentMonth + 1}`)
            .then(response => response.json())
            .then(events => {
                // Render events in the calendar
                renderEvents(events);
            })
            .catch(error => console.error('Error fetching events:', error));
    }

    // Function to render events in the calendar
    function renderEvents(events) {
        events.forEach(event => {
            const eventDate = new Date(event.calendar_date);
            console.log('Event Date:', eventDate);
            const dayElement = calendar.querySelector(`.day[data-day="${eventDate.getDate()}"]`);
            console.log('Day Element:', dayElement);
            if (dayElement) {
                const eventElement = document.createElement("div");
                eventElement.classList.add("event");
                eventElement.textContent = event.name; // Display the name field of the event
                console.log('Event Name:', event.name);
                dayElement.appendChild(eventElement);
            }
        });
    }
});
