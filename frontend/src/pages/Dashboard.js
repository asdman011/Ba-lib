// frontend/src/pages/Dashboard.js

import React, { useState } from 'react';
import './Dashboard.css';

const Dashboard = ({ ReadingProgress = { general_streak: 0 }, folders = [] }) => {
    const handlePageRead = (bookId, pagesRead) => {
        // fetch(`/books/${bookId}/progress/update/`, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //         'X-CSRFToken': getCookie('csrftoken') // Ensure CSRF token is available
        //     },
        //     body: JSON.stringify({ pages_read: pagesRead })
        // })
        // .then(response => response.json())
        // .then(data => {
        //     if (data.status === 'success') {
        //         console.log('Progress updated successfully');
        //     } else {
        //         console.error('Error updating progress:', data.message);
        //     }
        // })
        // .catch(error => console.error('Error:', error));
    };
    

    return (
        <div className="dashboard">
            <h1>Welcome to Your Dashboard</h1>
            <section className="streak">
                <h2>General Reading Streak: {ReadingProgress.general_streak}</h2>
            </section>
            {folders.map(folder => (
                <div key={folder.id} className="folder-section">
                    <h2>{folder.name} (Streak: {folder.streak_count} days)</h2>
                    {folder.books.map(book => (
                        <div key={book.id} className="book-card">
                            <img src={book.cover} alt={book.title} />
                            <h3>{book.title}</h3>
                            <p>Pages left: {book.pages_left}</p>
                            <p>{book.is_read ? 'Read' : 'In Progress'}</p>
                            {!book.is_read && (
                                <form onSubmit={() => handlePageRead(book.id)}>
                                    <input type="number" name="pages_read" placeholder="Pages read today" />
                                    <button type="submit">Update Progress</button>
                                </form>
                            )}
                        </div>
                    ))}
                </div>
            ))}
        </div>
    );
};

export default Dashboard;
