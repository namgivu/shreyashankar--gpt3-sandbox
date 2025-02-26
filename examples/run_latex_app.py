import os

from api import GPT, Example, UIConfig
from api import demo_web_app

# add gitcloned dir to PYTHONPATH
import sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


#region prepare :gpt
'''
GPT class to define GPT-related dataobj
mainpoint is list of Example obj w/ inp+out pair

then, final goal is to call 
#   = openai ie a py pkg
res = openai.Completion.create(engine, prompt, ...finetune_params)
#   =                         (        prompt ie plain text fr input@webapp
#   =                         (engine ie :codehere. gpt.engine

--- sumup
use :openai ie an OpenAI's py pkg
to call to OpenAI API endpoint w/  chosen :engine, :engine_params, training/priming example inp+out pairs 
to have output text fr input :prompt plaintext
'''
gpt = GPT(engine='davinci', temperature=0.5, max_tokens=100)

gpt.add_example(Example(inp='Two plus two equals four',                                     out='2 + 2 = 4'))
gpt.add_example(Example(inp='The integral from zero to infinity',                           out='\\int_0^{\\infty}'))
gpt.add_example(Example(inp='The gradient of x squared plus two times x with respect to x', out='\\nabla_x x^2 + 2x'))
gpt.add_example(Example(inp='The log of two times x',                                       out='\\log{2x}'))
gpt.add_example(Example(inp='x squared plus y squared plus equals z squared',               out='x^2 + y^2 = z^2'))
gpt.add_example(Example(inp='The sum from zero to twelve of i squared',                     out='\\sum_{i=0}^{12} i^2'))
gpt.add_example(Example(inp='E equals m times c squared',                                   out='E = mc^2'))
gpt.add_example(Example(inp='H naught of t',                                                out='H_0(t)'))
gpt.add_example(Example(inp='f of n equals 1 over (b-a) if n is 0 otherwise 5',             out='f(n) = \\begin{cases} 1/(b-a) &\\mbox{if } n \\equiv 0 \\\ # 5 \\end{cases}'))
#endregion prepare :gpt

demo_web_app(
    gpt    = gpt,
    config = UIConfig(
        description='Text to equation',
        button_text='Translate',
        placeholder='e.g. x squared plus 2 times x',
    ),
)
