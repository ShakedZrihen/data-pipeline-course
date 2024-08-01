/* eslint-disable react/prop-types */
import { Artist, ListenIcon, Position, Song, SongWrapper } from "./SongRow.style";

const SongRow = (props) => {
  const { song, position, artist, spotify_url } = props.song;

  return (
    <SongWrapper position={position}>
      <Position>{position}</Position>
      <Song>{song}</Song>
      <Artist>{artist}</Artist>
      <ListenIcon onClick={() => window.open(spotify_url, "_blank")} />
    </SongWrapper>
  );
};

export default SongRow;
