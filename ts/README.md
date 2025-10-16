This folder contains a minimal TypeScript sample for the AddonCource repo.

Commands (PowerShell):

# install dev dependencies
npm install --save-dev typescript ts-node

# build
npm run build

# run (after build)
npm start

# or run directly with ts-node
npm run dev

How to add & push this folder to the remote repo (run from the repository root):

# initialize (if needed) and push to remote
git init
# add remote only if not present:
# git remote add origin https://github.com/adithsath/AddonCource.git
git add ts
git commit -m "Add ts folder with TypeScript sample"
# create main branch if needed and push
git branch -M main
git push -u origin main

If you want, I can run the git commands for you from this environment (you may be prompted to authenticate)."}}]}EOF