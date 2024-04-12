import streamlit as st
import random

# Define user credentials and roles
users = {
    "admin": {"password": "admin123", "role": "admin"},
    # Student voters
    "bharani": {"password": "bharani123", "role": "student"},
    "vikram": {"password": "vikram123", "role": "student"},
    "rakesh": {"password": "rakesh123", "role": "student"},
    "rohith": {"password": "rohith123", "role": "student"},
}

# Election candidates
candidates = ['Naveen', 'Fawaz']

# Initialize session state for votes if not already present
if 'votes' not in st.session_state:
    st.session_state.votes = {candidate: 0 for candidate in candidates}

# Initialize session state for voted users if not already present
if 'voted_users' not in st.session_state:
    st.session_state.voted_users = {}

def login(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        st.session_state.username = username
        st.session_state.role = user['role']
        return True
    return False

def logout():
    for key in ['username', 'role']:
        if key in st.session_state:
            del st.session_state[key]

def calculate_winner():
    max_votes = max(st.session_state.votes.values())
    winners = [candidate for candidate, votes in st.session_state.votes.items() if votes == max_votes]
    return winners[0] if winners else "Draw"

def get_random_quote():
    quotes = [
        "Your vote is your voice.",
        "Every vote counts.",
        "Democracy is not just about voting, it’s about making our voices heard.",
        "Voting is the expression of our commitment to ourselves, one another, this country, and this world.",
        "Bad officials are elected by good citizens who do not vote.",
        "Voting is the first step towards building a better future.",
        "A vote is like a rifle: its usefulness depends upon the character of the user.",
        "The future of our democracy depends on your vote.",
        "Voting is the cornerstone of democracy.",
        "Don’t boo, vote!",
        "Your vote is your power.",
        "The ballot is stronger than the bullet.",
        "Elections belong to the people. It’s their decision.",
        "The vote is the most powerful nonviolent tool we have.",
        "The ignorance of one voter in a democracy impairs the security of all.",
        "Voting is not only our right—it is our power.",
        "Voting is the expression of our commitment to ourselves, one another, this country, and this world.",
        "If you don’t vote, you lose the right to complain.",
        "The ballot is stronger than the bullet.",
        "Democracy cannot succeed unless those who express their choice are prepared to choose wisely.",
        "The vote is the most powerful instrument ever devised by man for breaking down injustice.",
    ]
    return random.choice(quotes)

def main():
    st.markdown(
        """
        <style>
            body {
                background-color: #FFFFFF;
            }
            .header {
                color: #FFFFFF;
                background-color: #2196F3;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            }
            .subheader {
                color: #2196F3;
                background-color: #FFFFFF;
                padding: 5px;
                border-radius: 5px;
                text-align: center;
            }
            .info {
                color: #000000;
                background-color: #E0E0E0;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            }
            .quote {
                color: #000000;
                background-color: #FFEB3B;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            }
            .small-text {
                font-size: smaller;
                text-align: center;
            }
        </style>
        """
        , unsafe_allow_html=True
    )

    st.markdown('<p class="header">Voting by Agni College of Technology</p>', unsafe_allow_html=True)
    st.markdown('<p class="small-text">Voting conducted by Artificial Intelligence and Data Science</p>', unsafe_allow_html=True)

    st.sidebar.title("Login")
    
    if 'role' in st.session_state:
        st.sidebar.success(f"Logged in as {st.session_state.username}")
        if st.sidebar.button("Logout"):
            logout()
            st.sidebar.success("You've been logged out.")
            st.experimental_rerun()
    else:
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            if login(username, password):
                st.experimental_rerun()
            else:
                st.sidebar.error("Invalid username/password")

    if 'role' in st.session_state:
        if st.session_state.role == "admin":
            st.header("Vote Tally")
            for candidate, count in st.session_state.votes.items():
                st.write(f"{candidate}: {count} votes")

            st.subheader("Votes by Users")
            for user, voted_candidate in st.session_state.voted_users.items():
                st.write(f"{user}: Voted for {voted_candidate}")

            winner = calculate_winner()
            if winner == "Draw":
                st.subheader("Draw")
            else:
                st.subheader(f"Winner: {winner}")

        elif st.session_state.role == "student":
            st.header("Cast Your Vote")
            option = st.selectbox("Choose a candidate", candidates)
            if st.button("Vote"):
                st.session_state.votes[option] += 1
                st.success(f"You voted for {option}")
                st.session_state.voted_users[st.session_state.username] = option
                logout()  # Optional: Log out user after voting
                st.experimental_rerun()
    else:
        st.info("Please login to view this page.")

if __name__ == "__main__":
    main()

# Display random quote on the home page
quote = get_random_quote()
st.markdown(f'<p class="quote">{quote}</p>', unsafe_allow_html=True)
