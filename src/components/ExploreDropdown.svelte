<script>
import { goto } from '$app/navigation';

function handleSelect(event) {
    const value = event.target.value;
    if (value === 'title') {
        goto('/explore/title');
    } else if (value === 'artist') {
        goto('/explore/artist');
    }
}
</script>

<div class="explore-dropdown">
    <h1 class="dropdown-title">Explore by:</h1>
    <select on:change={handleSelect} class="dropdown">
        <option value="title">Title</option>
        <option value="artist">Artist</option>
    </select>
</div>

<style>
.explore-dropdown {
    display: flex;
    align-items: center;
    margin-right: 1rem;
}

.dropdown-title {
    color: #fff;
    font-size: 1.25rem;
    margin-right: 0.5rem;
}

.dropdown {
    font-size: 1.25rem;
    padding: 0.5rem;
    background-color: #2c2c2c;
    color: #fff;
    border: 2px solid #888;
    border-radius: 0;
    font-family: inherit;
}
</style>
