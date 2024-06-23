<script>
export let searchTerm = "";
export let searchBy = "title";
export let onSearchTermChange;
export let onSearchByChange;

function handleSearchTermChange(event) {
    if (onSearchTermChange) {
        onSearchTermChange(event.target.value);
    }
}

function handleSearchByChange(event) {
    if (onSearchByChange) {
        onSearchByChange(event.target.value);
    }
}
</script>

<div class="explore-input">
    <span class="explore-text">Explore by:</span>
    <select bind:value={searchBy} on:change={handleSearchByChange} class="dropdown">
        <option value="title">Title</option>
        <option value="artist">Artist</option>
    </select>
    <input type="text" bind:value={searchTerm} on:input={handleSearchTermChange} class="search-bar" placeholder="Search" />
</div>

<style>
.explore-input {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-left: 25px;
    margin-right: 25px;
}

.explore-text {
    color: white;
    font-size: 1.25rem;
}

.dropdown {
    padding: 0.5rem;
    font-size: 1rem;
    background-color: #2c2c2c;
    color: #fff;
    border: 2px solid #888;
    border-radius: 0.5rem;
    font-family: inherit;
}

.search-bar {
    flex: 1;
    padding: 0.5rem;
    font-size: 1rem;
    background-color: #2c2c2c;
    color: #fff;
    border: 2px solid #888;
    border-radius: 0.5rem;
    font-family: inherit;
}
</style>
