<script>
import AlbumCard from "../components/albumCard.svelte";
import * as albumsRawJson from '../../static/aotd_sheet_data_raw.json';
// import * as albumsRawJson from '../../static/tester_json.json';


const albumsJson = albumsRawJson.default;

let searchTerm = "";
let filteredAlbums = [];

// React to bound searchTerm and mutate the set of albums to display
$: {
    if(searchTerm){
        filteredAlbums = albumsJson.filter( album => album.name.toLowerCase().includes(searchTerm.toLowerCase()));
    }
    else {
        filteredAlbums = albumsJson;
    }
}

filteredAlbums = albumsRawJson;
</script>

<svelte:head>
	<title>Albums</title>
</svelte:head>
<input class="w-full rounded-md text-lg p-4 border-2 border-gray-500 bg-gray-100" bind:value={searchTerm} placeholder="Search Albums">
<!-- Default display grid -->
<div class="py-6 grid gap-5 md:grid-cols-4 grid-cols-1">
    {#each filteredAlbums as album}
        <AlbumCard album={album}/>
    {/each}
</div>
