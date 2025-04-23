set number
set autoindent
set smartindent
set expandtab
set tabstop=4
set shiftwidth=4
set smarttab
set hlsearch
set fileencodings=UTF-8,EUC-KR
set ruler
set title
set showmatch
set autowrite
set autoread
set ignorecase  
set smartcase   " Do not ignore case if capatals are included in the searching keyword
set backspace=indent,eol,start
set sidescroll=2
set sidescrolloff=10
set vb t_vb=     " No beep sound for errors
"set ambw=single
"set cursorline
"set gdefault   " Set global option (%s/foo/bar/g) default
set langmap=ㅁa,ㅠb,ㅊc,ㅇd,ㄷe,ㄹf,ㅎg,ㅗh,ㅑi,ㅓj,ㅏk,ㅣl,ㅡm,ㅜn,ㅐo,ㅔp,ㅂq,ㄱr,ㄴs,ㅅt,ㅕu,ㅍv,ㅈw,ㅌx,ㅛy,ㅋz

" Shortcuts for moving between splitted windows
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>


" Locate the cursor to where edited lastly
au BufReadPost *
\ if line("'\"") > 0 && line("'\"") <= line("$") |
\ exe "norm g`\"" |
\ endif

syntax on
colorscheme darkblue
