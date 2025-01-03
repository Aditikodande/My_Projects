const apiKey = 'c7b2d3486d804a7a0cce9eb37e7f6505'; // Your API Key
const searchButton = document.getElementById('search-btn');
const cityInput = document.getElementById('city-input');
const cityName = document.getElementById('city-name');
const currentTemp = document.getElementById('current-temp');
const weatherDescription = document.getElementById('weather-description');
const weatherIcon = document.getElementById('weather-icon');
const forecastContainer = document.getElementById('forecast-container');

// Event listener for search button
searchButton.addEventListener('click', () => {
    const city = cityInput.value.trim();
    if (city) {
        getWeatherData(city);
    }
});

// Function to fetch weather data
async function getWeatherData(city) {
    const currentWeatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;
    const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&units=metric&appid=${apiKey}`;

    try {
        // Fetch current weather data
        const currentWeatherResponse = await fetch(currentWeatherUrl);
        const currentWeatherData = await currentWeatherResponse.json();

        // Debugging: Check the response code and error message if available
        console.log('Current weather response:', currentWeatherData);

        if (currentWeatherData.cod !== 200) {
            // Display detailed error message from API
            alert(`Error: ${currentWeatherData.message}`);
            return;
        }

        // Display current weather data
        displayCurrentWeather(currentWeatherData);

        // Fetch forecast data
        const forecastResponse = await fetch(forecastUrl);
        const forecastData = await forecastResponse.json();

        // Display forecast data
        displayForecast(forecastData);
    } catch (error) {
        console.error('Error fetching data:', error);
        alert('Error fetching data. Please try again later.');
    }
}

// Function to display current weather data
function displayCurrentWeather(data) {
    cityName.textContent = `${data.name}, ${data.sys.country}`;
    currentTemp.textContent = `Temperature: ${data.main.temp}°C`;
    weatherDescription.textContent = data.weather[0].description;
    weatherIcon.src = `https://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
}

// Function to display weather forecast
function displayForecast(data) {
    forecastContainer.innerHTML = ''; // Clear previous forecast data

    // Loop through forecast data (every 3 hours)
    data.list.filter((_, index) => index % 8 === 0).forEach(item => {
        const forecastItem = document.createElement('div');
        forecastItem.classList.add('forecast-item');

        const date = new Date(item.dt * 1000);
        const time = `${date.getHours()}:${date.getMinutes()}`;

        forecastItem.innerHTML = `
            <p>${time}</p>
            <img src="https://openweathermap.org/img/wn/${item.weather[0].icon}.png" alt="weather icon">
            <p>${item.main.temp}°C</p>
        `;
        forecastContainer.appendChild(forecastItem);
    });
}
