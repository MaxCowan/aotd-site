<script>
import ExploreInput from '../../../components/ExploreInput.svelte';
import TitleView from '../../../components/TitleView.svelte';

let searchTerm = "";
let searchBy = "title";

function handleSearchTermChange(newTerm) {
    console.log('Search term changed:', newTerm);
    searchTerm = newTerm;
}

function handleSearchByChange(newSearchBy) {
    searchBy = newSearchBy;
    if (searchBy === "artist") {
        window.location.href = "/explore/artist";
    }
}
</script>

<svelte:head>
    <title>Explore by Title</title>
</svelte:head>

<div class="container">
    <ExploreInput
        {searchTerm}
        {searchBy}
        onSearchTermChange={handleSearchTermChange}
        onSearchByChange={handleSearchByChange}
    />
    <div class="content">
        <TitleView {searchTerm} />
    </div>
</div>

<style>
.container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100vh;
    box-sizing: border-box;
    padding: 25px;
}

.content {
    flex: 1;
    overflow-y: auto;
}
</style>
