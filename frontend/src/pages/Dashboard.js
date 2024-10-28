// frontend/src/pages/Dashboard.js

import React, { useEffect, useState } from 'react';
import './Dashboard.css';

const Dashboard = () => {
    // Placeholder data
    const [books, setBooks] = useState([
        { id: 1, title: "Book 1" },
        { id: 2, title: "Book 2" }
    ]);
    
    const [folders, setFolders] = useState([
        { id: 1, name: "Folder 1" },
        { id: 2, name: "Folder 2" }
    ]);

    const [streak, setStreak] = useState(10);  // Placeholder streak

    return (
        <div className="dashboard">
            <h1>Welcome to Your Dashboard</h1>

            <section className="dashboard-section books">
                <h2>Your Books</h2>
                <div className="items-grid">
                    {books.map(book => (
                        <div className="item-card" key={book.id}>{book.title}</div>
                    ))}
                </div>
            </section>

            <section className="dashboard-section folders">
                <h2>Your Folders</h2>
                <div className="items-grid">
                    {folders.map(folder => (
                        <div className="item-card" key={folder.id}>{folder.name}</div>
                    ))}
                </div>
            </section>

            <section className="dashboard-section streaks">
                <h2>Reading Streak</h2>
                <p>You have a {streak}-day streak! Keep it up!</p>
            </section>
        </div>
    );
};

export default Dashboard;
