<script>
import {albums, fetchSheetAlbums} from "../albumstore";
import AlbumCard from "../components/albumCard.svelte";


let searchTerm = "";
let filteredAlbums = [];

// React to bound searchTerm and mutate the set of albums to display
$: {
    if(searchTerm){
        filteredAlbums = $albums.filter( album => album.albumName.toLowerCase().includes(searchTerm.toLowerCase()));
    }
    else {
        filteredAlbums = [...$albums];
    }
}

fetchSheetAlbums();

</script>

<svelte:head>
	<title>Albums</title>
</svelte:head>
<input class="w-full rounded-md text-lg p-4 border-2 border-gray-200" bind:value={searchTerm} placeholder="Search Albums">
<!-- Default display grid -->
<div class="py-4 grid gap-4 md:grid-cols-4 grid-cols-1">
    {#each filteredAlbums as album}
        <AlbumCard album={album}/>
    {/each}
</div>
