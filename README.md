# Cross-Platform interface for running ttsmms desktop

## Install
1. clone this repo
```bash
git clone https://github.com/NoerNova/vits-tts-interface-gui.git
```

2. download and extract models
```bash
# to download models see
https://github.com/facebookresearch/fairseq/tree/main/examples/mms#tts
```
and extract to ``src/vits_tts_interface_gui/models``

3. using python venv is recomments (I use miniconda)
```bash
# conda install construct see
# https://docs.conda.io/en/latest/miniconda.html
conda create shntts python=3.8
```

4. install requirements
```bash
# goto root dir
python -m pip install -r requirements.txt
```

## Dev
1. make sure to install briefcase
```bash
pip install briefcase
```

2. run dev mode
```bash
briefcase dev
```

## Build and Packs
1. create
```bash
briefcase create
```

2. build
```bash
briefcase build
```

3. package
```bash
briefcase --adhoc-sign
```

***see full Beeware Tutorial*** https://docs.beeware.org/en/latest/

## License
MIT
