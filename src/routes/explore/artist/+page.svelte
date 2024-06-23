<script>
import ExploreInput from '../../../components/ExploreInput.svelte';
import ArtistView from '../../../components/ArtistView.svelte';

let searchTerm = "";
let searchBy = "artist";

function handleSearchTermChange(newTerm) {
    console.log('Search term changed:', newTerm);
    searchTerm = newTerm;
}

function handleSearchByChange(newSearchBy) {
    searchBy = newSearchBy;
    if (searchBy === "title") {
        window.location.href = "/explore/title";
    }
}
</script>

<svelte:head>
    <title>Explore by Artist</title>
</svelte:head>

<div class="container">
    <ExploreInput
        {searchTerm}
        {searchBy}
        onSearchTermChange={handleSearchTermChange}
        onSearchByChange={handleSearchByChange}
    />
    <div class="content">
        <ArtistView {searchTerm} />
    </div>
</div>

<style>
.container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100vh;
    box-sizing: border-box;
}

.content {
    flex: 1;
    overflow-y: auto;
}
</style>
