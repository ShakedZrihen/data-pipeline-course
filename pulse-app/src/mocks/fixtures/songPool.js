const songPool = [
  {
    song: "Blinding Lights",
    artist: "The Weeknd",
    album: "After Hours",
    duration: "3:20",
    spotify_url: "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b",
    songFeatures: { key: "F# Minor", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Watermelon Sugar",
    artist: "Harry Styles",
    album: "Fine Line",
    duration: "2:54",
    spotify_url: "https://open.spotify.com/track/6UelLqGlWMcVH1E5c4H7lY",
    songFeatures: { key: "D Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Levitating",
    artist: "Dua Lipa",
    album: "Future Nostalgia",
    duration: "3:23",
    spotify_url: "https://open.spotify.com/track/463CkQjx2Zk1yXoBuierM9",
    songFeatures: { key: "B Minor", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Save Your Tears",
    artist: "The Weeknd",
    album: "After Hours",
    duration: "3:36",
    spotify_url: "https://open.spotify.com/track/5QO79kh1waicV47BqGRL3g",
    songFeatures: { key: "C Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Good 4 U",
    artist: "Olivia Rodrigo",
    album: "SOUR",
    duration: "2:58",
    spotify_url: "https://open.spotify.com/track/4ZtFanR9U6ndgddUvNcjcG",
    songFeatures: { key: "F# Minor", genre: "Pop Rock", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Peaches",
    artist: "Justin Bieber",
    album: "Justice",
    duration: "3:18",
    spotify_url: "https://open.spotify.com/track/4uChbGZ6u3Rf90SCiOqyrY",
    songFeatures: { key: "C Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "MONTERO (Call Me By Your Name)",
    artist: "Lil Nas X",
    album: "MONTERO",
    duration: "2:17",
    spotify_url: "https://open.spotify.com/track/67BtfxlNbhBmCDR2L2l8qd",
    songFeatures: { key: "C# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Drivers License",
    artist: "Olivia Rodrigo",
    album: "SOUR",
    duration: "4:02",
    spotify_url: "https://open.spotify.com/track/6PERP62TejQjgHu81z2K9R",
    songFeatures: { key: "B Flat Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Kiss Me More",
    artist: "Doja Cat",
    album: "Planet Her",
    duration: "3:28",
    spotify_url: "https://open.spotify.com/track/748mdHapucXQri7IAO8yFK",
    songFeatures: { key: "A Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Leave The Door Open",
    artist: "Bruno Mars",
    album: "An Evening With Silk Sonic",
    duration: "4:02",
    spotify_url: "https://open.spotify.com/track/7MAibcTli4IisCtbHKrGMh",
    songFeatures: { key: "C Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Stay",
    artist: "The Kid LAROI",
    album: "F*CK LOVE 3: OVER YOU",
    duration: "2:21",
    spotify_url: "https://open.spotify.com/track/5PjdY0CKGZdEuoNab3yDmX",
    songFeatures: { key: "A Minor", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Industry Baby",
    artist: "Lil Nas X",
    album: "MONTERO",
    duration: "3:32",
    spotify_url: "https://open.spotify.com/track/27NovPIUIRrOZoCHxABJwK",
    songFeatures: { key: "A Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Heat Waves",
    artist: "Glass Animals",
    album: "Dreamland",
    duration: "3:58",
    spotify_url: "https://open.spotify.com/track/02MWAaffLxlfxAUY7c5dvx",
    songFeatures: { key: "F# Major", genre: "Alternative", language: "English" },
    artistFeatures: { type: "Band" }
  },
  {
    song: "Deja Vu",
    artist: "Olivia Rodrigo",
    album: "SOUR",
    duration: "3:35",
    spotify_url: "https://open.spotify.com/track/6HU7h9RYOaPRFeh0R3UeAr",
    songFeatures: { key: "A Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Good Days",
    artist: "SZA",
    album: "Good Days",
    duration: "4:39",
    spotify_url: "https://open.spotify.com/track/3YJJjQPAbDT7mGpX3WtQ9A",
    songFeatures: { key: "E Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Go Crazy",
    artist: "Chris Brown",
    album: "Slime & B",
    duration: "2:57",
    spotify_url: "https://open.spotify.com/track/1IIKrJVP1C9N7iPtG6eOsK",
    songFeatures: { key: "C Major", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Positions",
    artist: "Ariana Grande",
    album: "Positions",
    duration: "2:52",
    spotify_url: "https://open.spotify.com/track/35mvY5S1H3J2QZyna3TFe0",
    songFeatures: { key: "A Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Need To Know",
    artist: "Doja Cat",
    album: "Planet Her",
    duration: "3:30",
    spotify_url: "https://open.spotify.com/track/3DarAbFujv6eYNliUTyqtz",
    songFeatures: { key: "A Minor", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Rockstar",
    artist: "DaBaby",
    album: "Blame It On Baby",
    duration: "3:01",
    spotify_url: "https://open.spotify.com/track/1i1fxkWeaMmKEB4T7zqbzK",
    songFeatures: { key: "C# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "What's Next",
    artist: "Drake",
    album: "Scary Hours 2",
    duration: "2:58",
    spotify_url: "https://open.spotify.com/track/5JZ9KJZvTGJhQ5XS6v8kP0",
    songFeatures: { key: "C# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Famous Friends",
    artist: "Chris Young",
    album: "Famous Friends",
    duration: "2:45",
    spotify_url: "https://open.spotify.com/track/6gLDFfBv54A7A2F5pR5ED4",
    songFeatures: { key: "C Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Wasted On You",
    artist: "Morgan Wallen",
    album: "Dangerous: The Double Album",
    duration: "2:58",
    spotify_url: "https://open.spotify.com/track/5uCax9HTNlzGybIStD3vDh",
    songFeatures: { key: "A Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Sand In My Boots",
    artist: "Morgan Wallen",
    album: "Dangerous: The Double Album",
    duration: "3:21",
    spotify_url: "https://open.spotify.com/track/2xLMifQCjDGFmkHkpNLD9h",
    songFeatures: { key: "G Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Chasing After You",
    artist: "Ryan Hurd",
    album: "Chasing After You",
    duration: "3:28",
    spotify_url: "https://open.spotify.com/track/7FrGJaubt4L4jdSJNQX3kE",
    songFeatures: { key: "E Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "One Too Many",
    artist: "Keith Urban",
    album: "The Speed Of Now Part 1",
    duration: "3:25",
    spotify_url: "https://open.spotify.com/track/3HcmIdlUpC9tI9qSRPs2rH",
    songFeatures: { key: "C# Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Fancy Like",
    artist: "Walker Hayes",
    album: "Country Stuff",
    duration: "2:41",
    spotify_url: "https://open.spotify.com/track/0ztDBwFJws6AZj6ucTpFyV",
    songFeatures: { key: "C Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Glad You Exist",
    artist: "Dan + Shay",
    album: "Good Things",
    duration: "2:25",
    spotify_url: "https://open.spotify.com/track/7rZYS3j3ESzCUH1A2Tm4dA",
    songFeatures: { key: "F Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Band" }
  },
  {
    song: "Starting Over",
    artist: "Chris Stapleton",
    album: "Starting Over",
    duration: "4:00",
    spotify_url: "https://open.spotify.com/track/0aaJbSgJT4YCgsGNG3dPhe",
    songFeatures: { key: "A Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Drunk (And I Don't Wanna Go Home)",
    artist: "Elle King",
    album: "Drunk (And I Don't Wanna Go Home)",
    duration: "4:05",
    spotify_url: "https://open.spotify.com/track/2h4cmbybE5bFWzy5GVwrrY",
    songFeatures: { key: "C Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "WAP",
    artist: "Cardi B",
    album: "Invasion Of Privacy",
    duration: "3:07",
    spotify_url: "https://open.spotify.com/track/4Oun2ylbjFKMPTiaSbbCih",
    songFeatures: { key: "C Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "The Box",
    artist: "Roddy Ricch",
    album: "Please Excuse Me For Being Antisocial",
    duration: "3:16",
    spotify_url: "https://open.spotify.com/track/0nbXyq5TXYPCO7pr3N8S4I",
    songFeatures: { key: "F# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "For The Night",
    artist: "Pop Smoke",
    album: "Shoot For The Stars Aim For The Moon",
    duration: "3:10",
    spotify_url: "https://open.spotify.com/track/35MvY5S1H3J2QZyna3TFe0",
    songFeatures: { key: "A Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "What's Poppin",
    artist: "Jack Harlow",
    album: "Sweet Action",
    duration: "2:19",
    spotify_url: "https://open.spotify.com/track/2rJojRUND9wOvtRVRGUzEt",
    songFeatures: { key: "G Major", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Savage Love",
    artist: "Jawsh 685",
    album: "Savage Love",
    duration: "2:51",
    spotify_url: "https://open.spotify.com/track/4P6IttK2PRBjyr3fm0pP7t",
    songFeatures: { key: "A Minor", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Dynamite",
    artist: "BTS",
    album: "BE",
    duration: "3:19",
    spotify_url: "https://open.spotify.com/track/1pKyNzJyU7lyFNdHe3lT7A",
    songFeatures: { key: "C# Minor", genre: "Pop", language: "Korean" },
    artistFeatures: { type: "Band" }
  },
  {
    song: "Therefore I Am",
    artist: "Billie Eilish",
    album: "Happier Than Ever",
    duration: "2:54",
    spotify_url: "https://open.spotify.com/track/54bFM56PmE4YLRnqpW6Tha",
    songFeatures: { key: "C# Minor", genre: "Alternative", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Willow",
    artist: "Taylor Swift",
    album: "evermore",
    duration: "3:34",
    spotify_url: "https://open.spotify.com/track/2VxeLyX666F8uXCJ0dZF8B",
    songFeatures: { key: "E Minor", genre: "Folk", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Drivers License",
    artist: "Olivia Rodrigo",
    album: "SOUR",
    duration: "4:02",
    spotify_url: "https://open.spotify.com/track/6PERP62TejQjgHu81z2K9R",
    songFeatures: { key: "B Flat Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Positions",
    artist: "Ariana Grande",
    album: "Positions",
    duration: "2:52",
    spotify_url: "https://open.spotify.com/track/35mvY5S1H3J2QZyna3TFe0",
    songFeatures: { key: "A Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Levitating",
    artist: "Dua Lipa",
    album: "Future Nostalgia",
    duration: "3:23",
    spotify_url: "https://open.spotify.com/track/2LBqCSwhJGcFQeTHMVGwy3",
    songFeatures: { key: "B Minor", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Good 4 U",
    artist: "Olivia Rodrigo",
    album: "SOUR",
    duration: "2:58",
    spotify_url: "https://open.spotify.com/track/4ZtFanR9U6ndgddUvNcjcG",
    songFeatures: { key: "F# Minor", genre: "Pop Rock", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Kiss Me More",
    artist: "Doja Cat",
    album: "Planet Her",
    duration: "3:28",
    spotify_url: "https://open.spotify.com/track/748mdHapucXQri7IAO8yFK",
    songFeatures: { key: "A Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Heartbreak Anniversary",
    artist: "Giveon",
    album: "TAKE TIME",
    duration: "3:18",
    spotify_url: "https://open.spotify.com/track/2N4t5x0YyY9rOmyCzxJ3Sk",
    songFeatures: { key: "A Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Peaches",
    artist: "Justin Bieber",
    album: "Justice",
    duration: "3:18",
    spotify_url: "https://open.spotify.com/track/4uChbGZ6u3Rf90SCiOqyrY",
    songFeatures: { key: "C Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Montero (Call Me By Your Name)",
    artist: "Lil Nas X",
    album: "MONTERO",
    duration: "2:17",
    spotify_url: "https://open.spotify.com/track/67BtfxlNbhBmCDR2L2l8qd",
    songFeatures: { key: "C# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Save Your Tears",
    artist: "The Weeknd",
    album: "After Hours",
    duration: "3:36",
    spotify_url: "https://open.spotify.com/track/5QO79kh1waicV47BqGRL3g",
    songFeatures: { key: "C Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Levitating",
    artist: "Dua Lipa",
    album: "Future Nostalgia",
    duration: "3:23",
    spotify_url: "https://open.spotify.com/track/463CkQjx2Zk1yXoBuierM9",
    songFeatures: { key: "B Minor", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Leave The Door Open",
    artist: "Bruno Mars",
    album: "An Evening With Silk Sonic",
    duration: "4:02",
    spotify_url: "https://open.spotify.com/track/7MAibcTli4IisCtbHKrGMh",
    songFeatures: { key: "C Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Mood",
    artist: "24kGoldn",
    album: "El Dorado",
    duration: "2:20",
    spotify_url: "https://open.spotify.com/track/4jAIqgrPjKLTY9Gbez25Qb",
    songFeatures: { key: "A Major", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Laugh Now Cry Later",
    artist: "Drake",
    album: "Certified Lover Boy",
    duration: "4:21",
    spotify_url: "https://open.spotify.com/track/2Sa0a4VMwI9VEG4uGoMaN1",
    songFeatures: { key: "C# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Heat Waves",
    artist: "Glass Animals",
    album: "Dreamland",
    duration: "3:58",
    spotify_url: "https://open.spotify.com/track/02MWAaffLxlfxAUY7c5dvx",
    songFeatures: { key: "F# Major", genre: "Alternative", language: "English" },
    artistFeatures: { type: "Band" }
  },
  {
    song: "Deja Vu",
    artist: "Olivia Rodrigo",
    album: "SOUR",
    duration: "3:35",
    spotify_url: "https://open.spotify.com/track/6HU7h9RYOaPRFeh0R3UeAr",
    songFeatures: { key: "A Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Good Days",
    artist: "SZA",
    album: "Good Days",
    duration: "4:39",
    spotify_url: "https://open.spotify.com/track/3YJJjQPAbDT7mGpX3WtQ9A",
    songFeatures: { key: "E Major", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Go Crazy",
    artist: "Chris Brown",
    album: "Slime & B",
    duration: "2:57",
    spotify_url: "https://open.spotify.com/track/1IIKrJVP1C9N7iPtG6eOsK",
    songFeatures: { key: "C Major", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Positions",
    artist: "Ariana Grande",
    album: "Positions",
    duration: "2:52",
    spotify_url: "https://open.spotify.com/track/35mvY5S1H3J2QZyna3TFe0",
    songFeatures: { key: "A Major", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Need To Know",
    artist: "Doja Cat",
    album: "Planet Her",
    duration: "3:30",
    spotify_url: "https://open.spotify.com/track/3DarAbFujv6eYNliUTyqtz",
    songFeatures: { key: "A Minor", genre: "R&B", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Rockstar",
    artist: "DaBaby",
    album: "Blame It On Baby",
    duration: "3:01",
    spotify_url: "https://open.spotify.com/track/1i1fxkWeaMmKEB4T7zqbzK",
    songFeatures: { key: "C# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "What's Next",
    artist: "Drake",
    album: "Scary Hours 2",
    duration: "2:58",
    spotify_url: "https://open.spotify.com/track/5JZ9KJZvTGJhQ5XS6v8kP0",
    songFeatures: { key: "C# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Famous Friends",
    artist: "Chris Young",
    album: "Famous Friends",
    duration: "2:45",
    spotify_url: "https://open.spotify.com/track/6gLDFfBv54A7A2F5pR5ED4",
    songFeatures: { key: "C Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Wasted On You",
    artist: "Morgan Wallen",
    album: "Dangerous: The Double Album",
    duration: "2:58",
    spotify_url: "https://open.spotify.com/track/5uCax9HTNlzGybIStD3vDh",
    songFeatures: { key: "A Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Sand In My Boots",
    artist: "Morgan Wallen",
    album: "Dangerous: The Double Album",
    duration: "3:21",
    spotify_url: "https://open.spotify.com/track/2xLMifQCjDGFmkHkpNLD9h",
    songFeatures: { key: "G Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Chasing After You",
    artist: "Ryan Hurd",
    album: "Chasing After You",
    duration: "3:28",
    spotify_url: "https://open.spotify.com/track/7FrGJaubt4L4jdSJNQX3kE",
    songFeatures: { key: "E Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "One Too Many",
    artist: "Keith Urban",
    album: "The Speed Of Now Part 1",
    duration: "3:25",
    spotify_url: "https://open.spotify.com/track/3HcmIdlUpC9tI9qSRPs2rH",
    songFeatures: { key: "C# Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Fancy Like",
    artist: "Walker Hayes",
    album: "Country Stuff",
    duration: "2:41",
    spotify_url: "https://open.spotify.com/track/0ztDBwFJws6AZj6ucTpFyV",
    songFeatures: { key: "C Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Glad You Exist",
    artist: "Dan + Shay",
    album: "Good Things",
    duration: "2:25",
    spotify_url: "https://open.spotify.com/track/7rZYS3j3ESzCUH1A2Tm4dA",
    songFeatures: { key: "F Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Band" }
  },
  {
    song: "Starting Over",
    artist: "Chris Stapleton",
    album: "Starting Over",
    duration: "4:00",
    spotify_url: "https://open.spotify.com/track/0aaJbSgJT4YCgsGNG3dPhe",
    songFeatures: { key: "A Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Drunk (And I Don't Wanna Go Home)",
    artist: "Elle King",
    album: "Drunk (And I Don't Wanna Go Home)",
    duration: "4:05",
    spotify_url: "https://open.spotify.com/track/2h4cmbybE5bFWzy5GVwrrY",
    songFeatures: { key: "C Major", genre: "Country", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "WAP",
    artist: "Cardi B",
    album: "Invasion Of Privacy",
    duration: "3:07",
    spotify_url: "https://open.spotify.com/track/4Oun2ylbjFKMPTiaSbbCih",
    songFeatures: { key: "C Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "The Box",
    artist: "Roddy Ricch",
    album: "Please Excuse Me For Being Antisocial",
    duration: "3:16",
    spotify_url: "https://open.spotify.com/track/0nbXyq5TXYPCO7pr3N8S4I",
    songFeatures: { key: "F# Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "For The Night",
    artist: "Pop Smoke",
    album: "Shoot For The Stars Aim For The Moon",
    duration: "3:10",
    spotify_url: "https://open.spotify.com/track/35MvY5S1H3J2QZyna3TFe0",
    songFeatures: { key: "A Minor", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "What's Poppin",
    artist: "Jack Harlow",
    album: "Sweet Action",
    duration: "2:19",
    spotify_url: "https://open.spotify.com/track/2rJojRUND9wOvtRVRGUzEt",
    songFeatures: { key: "G Major", genre: "Hip Hop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Savage Love",
    artist: "Jawsh 685",
    album: "Savage Love",
    duration: "2:51",
    spotify_url: "https://open.spotify.com/track/4P6IttK2PRBjyr3fm0pP7t",
    songFeatures: { key: "A Minor", genre: "Pop", language: "English" },
    artistFeatures: { type: "Solo", gender: "Male" }
  },
  {
    song: "Dynamite",
    artist: "BTS",
    album: "BE",
    duration: "3:19",
    spotify_url: "https://open.spotify.com/track/1pKyNzJyU7lyFNdHe3lT7A",
    songFeatures: { key: "C# Minor", genre: "Pop", language: "Korean" },
    artistFeatures: { type: "Band" }
  },
  {
    song: "Therefore I Am",
    artist: "Billie Eilish",
    album: "Happier Than Ever",
    duration: "2:54",
    spotify_url: "https://open.spotify.com/track/54bFM56PmE4YLRnqpW6Tha",
    songFeatures: { key: "C# Minor", genre: "Alternative", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  },
  {
    song: "Willow",
    artist: "Taylor Swift",
    album: "evermore",
    duration: "3:34",
    spotify_url: "https://open.spotify.com/track/2VxeLyX666F8uXCJ0dZF8B",
    songFeatures: { key: "E Minor", genre: "Folk", language: "English" },
    artistFeatures: { type: "Solo", gender: "Female" }
  }
];

export default songPool;
