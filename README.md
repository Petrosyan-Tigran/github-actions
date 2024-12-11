# github-actions

cd using_actions/ 

npx create-react-app --template typescript react-app

cd react-app/

npm start

npm install @actions/core@1.10.1 @actions/exec@1.1.1 @actions/github@6.0.0 --save-exact

python3 -m venv venv

pip freeze > requirements.txt
