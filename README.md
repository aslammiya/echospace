# echoSpace

A web application built with Django Channels, Tailwind CSS, and WebSocket, allowing users to create accounts, join rooms, and chat in real-time.

## Features

- **User Authentication**: Register, log in, and manage account details.
- **Profile Management**: Update first name, last name, username, and profile picture.
- **Room Management**: Create and join voice rooms.
- **Real-Time Chat**: Communicate with others in the same room.
- **User List**: View a list of all registered users.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS, AJAX
- **Real-Time Communication**: WebSocket, Django Channels
- **Database**: SQLite3
- **Redis**: Caching layer for frequently accessed data. 
- **Development Tools**: Postman
## Screenshots
<div style="text-align: center; margin-bottom: 20px;">
  <img src="media/screenshots/ds_1.png" alt="Main Screenshot" style="height: auto; border: 1px solid #ddd; border-radius: 5px;">
</div>
<div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 5%;">
  <img src="media/screenshots/ph_1.png" alt="Thumbnail 1" style="width: 20%; height: auto; border: 1px solid #ddd; border-radius: 5px; ">
  <img src="media/screenshots/ph_2.png" alt="Thumbnail 3" style="width: 20%; height: auto; border: 1px solid #ddd; border-radius: 5px; ">
  <img src="media/screenshots/ph_3.png" alt="Thumbnail 5" style="width: 20%; height: auto; border: 1px solid #ddd; border-radius: 5px; ">
  <img src="media/screenshots/ph_5.png" alt="Thumbnail 5" style="width: 20%; height: auto; border: 1px solid #ddd; border-radius: 5px; ">
  <img src="media/screenshots/ph_6.png" alt="Thumbnail 5" style="width: 20%; height: auto; border: 1px solid #ddd; border-radius: 5px; ">

</div>
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 5%; margin-top:20px">
  <img src="media/screenshots/ds_2.png" alt="Thumbnail 1" style="width: 50%; height: auto; border: 1px solid #ddd; border-radius: 5px;">
  <img src="media/screenshots/ds_3.png" alt="Thumbnail 3" style="width: 50%; height: auto; border: 1px solid #ddd; border-radius: 5px;">
</div>

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Set Up Virtual Environment**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database**

   ```bash
   ./manage.py migrate
   ```

5. **Create Superuser**

   ```bash
   ./manage.py createsuperuser
   ```

6. **Configure Redis**

   - **For Local Development**: Uncomment the following lines in `core/settings.py` and comment out the `REDIS_URL` section.

     ```python
     CHANNEL_LAYERS = {
         "default": {
             "BACKEND": "channels_redis.core.RedisChannelLayer",
             "CONFIG": {
                 "hosts": [("localhost", 6379)],
             },
         },
     }
     ```

   - **For Production**: Uncomment the `REDIS_URL` line and comment out the local configuration.

     ```python
     REDIS_URL = os.environ.get('REDIS_URL')

     CHANNEL_LAYERS = {
         "default": {
             "BACKEND": "channels_redis.core.RedisChannelLayer",
             "CONFIG": {
                 "hosts": [REDIS_URL],
             },
         },
     }
     ```

   Set the `REDIS_URL` environment variable to your Redis instance URL in production environments like Heroku or Render. Example:

   ```bash
   export REDIS_URL="redis://:your_redis_password@your_redis_host:port/0"
   ```

7. **Run the Application**

   ```bash
   daphne -b 0.0.0.0 -p 8789 core.asgi:application
   ```

   Or with Gunicorn:

   ```bash
   gunicorn -k daphne -b 0.0.0.0:8000 core.asgi:application
   ```

## Usage

- **Access the Web App**: Open your browser and navigate to `http://localhost:8789` (or the port you specified).
- **Log In / Register**: Use the provided forms to create an account or log in.
- **Create / Join Rooms**: Use the left-side panel to manage and join voice rooms.
- **Chat in Rooms**: Communicate with other users in the same room.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Replace placeholders like `https://github.com/yourusername/your-repository.git` with your actual repository URL. Adjust any specifics as needed for your project.