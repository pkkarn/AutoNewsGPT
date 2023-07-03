from chain.agents import agent

def test(str):
    result = agent.run(input=str)
    return result


print(test('Give me latest'))