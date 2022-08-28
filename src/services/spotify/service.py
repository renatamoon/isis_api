# PROJECT IMPORTS
from src.transport.spotify.playlist_transport.transport import GetPlaylistsFromSpotify


class SpotifyPlaylistsService:

    playlists = GetPlaylistsFromSpotify

    @classmethod
    def party_playlist_objects(cls) -> list:

        musics = cls.playlists.get_party_playlist()

        response_music = cls.__get_list_of_music_response(
            musics=musics
        )

        return response_music

    @classmethod
    def pop_playlist_objects(cls) -> list:

        musics = cls.playlists.get_pop_playlist()

        response_music = cls.__get_list_of_music_response(
            musics=musics
        )

        return response_music

    @classmethod
    def rock_playlist_objects(cls) -> list:

        musics = cls.playlists.get_rock_playlist()

        response_music = cls.__get_list_of_music_response(
            musics=musics
        )

        return response_music

    @classmethod
    def classic_playlist_objects(cls) -> list:

        musics = cls.playlists.get_classic_playlist()

        response_music = cls.__get_list_of_music_response(
            musics=musics
        )

        return response_music

    @classmethod
    def __get_list_of_music_response(cls, musics: dict) -> list:
        music_list = []

        for dict_item in musics.get("items"):
            id_music = dict_item.get("track").get("id")
            artist_name = dict_item.get("track").get("album").get("artists").pop().get("name")
            music_name = dict_item.get("track").get("name")
            album_name = dict_item.get("track").get("album").get("name")

            musics_dict = {
                "music_id": id_music,
                "artist_name": artist_name,
                "music_name": music_name,
                "album_name": album_name
            }

            music_list.append(musics_dict)

        return music_list
